#!/usr/bin/env python3
"""
FoneClaw v3 — Static site builder with Jinja2 templates and incremental builds.

Usage:
    python3 build.py                    # Build all (incremental)
    python3 build.py --lang zh          # Build one language
    python3 build.py --page features    # Build one page type
    python3 build.py --force            # Force full rebuild
    python3 build.py --dry-run          # Preview what would be rebuilt
"""

import os, sys, json, hashlib, argparse, time, re, copy
from pathlib import Path
from datetime import datetime

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    print("ERROR: Jinja2 not installed. Run: pip install jinja2")
    sys.exit(1)

# === Config ===
BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / 'templates'
I18N_DIR = BASE_DIR / 'i18n'
COMPONENTS_DIR = BASE_DIR / 'components'
ARTICLES_DIR = BASE_DIR / 'articles'
OUTPUT_DIR = BASE_DIR / 'output'
CACHE_DIR = BASE_DIR / '_build_cache'
HASHES_FILE = CACHE_DIR / 'hashes.json'

SITE_URL = 'https://www.foneclaw.ai'

LANGUAGES = {
    'en': {'name': 'English', 'native': 'English', 'dir': '', 'hreflang': 'en'},
    'zh': {'name': 'Chinese (Simplified)', 'native': '简体中文', 'dir': 'zh', 'hreflang': 'zh'},
    'tw': {'name': 'Traditional Chinese', 'native': '繁體中文', 'dir': 'tw', 'hreflang': 'zh-TW'},
    'ja': {'name': 'Japanese', 'native': '日本語', 'dir': 'ja', 'hreflang': 'ja'},
    'ko': {'name': 'Korean', 'native': '한국어', 'dir': 'ko', 'hreflang': 'ko'},
    'es': {'name': 'Spanish', 'native': 'Español', 'dir': 'es', 'hreflang': 'es'},
    'pt': {'name': 'Portuguese', 'native': 'Português', 'dir': 'pt', 'hreflang': 'pt'},
    'ru': {'name': 'Russian', 'native': 'Русский', 'dir': 'ru', 'hreflang': 'ru'},
    'fr': {'name': 'French', 'native': 'Français', 'dir': 'fr', 'hreflang': 'fr'},
    'de': {'name': 'German', 'native': 'Deutsch', 'dir': 'de', 'hreflang': 'de'},
    'ar': {'name': 'Arabic', 'native': 'العربية', 'dir': 'ar', 'hreflang': 'ar'},
    'th': {'name': 'Thai', 'native': 'ไทย', 'dir': 'th', 'hreflang': 'th'},
    'vi': {'name': 'Vietnamese', 'native': 'Tiếng Việt', 'dir': 'vi', 'hreflang': 'vi'},
    'id': {'name': 'Indonesian', 'native': 'Bahasa Indonesia', 'dir': 'id', 'hreflang': 'id'},
}

PAGES = ['index', 'features', 'download', 'resources', 'community', 'privacy', 'cookie']
HUB_PAGES = ['voice-control', 'comparisons', 'ai-agent', 'news']
SUB_HUB_PAGES = {
    'comparisons': ['tech-analysis', 'foneclaw-vs'],
    'ai-agent': ['gemini-intelligence', 'other'],
}


# === Loaders ===

def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def load_translations():
    """Load all 14 language JSON files."""
    translations = {}
    for lang in LANGUAGES:
        path = I18N_DIR / f'{lang}.json'
        if path.exists():
            translations[lang] = load_json(path)
        else:
            print(f"  WARNING: Missing translation file: {path}")
    return translations


def load_components():
    """Load nav.json, footer.json, social.json."""
    nav = load_json(COMPONENTS_DIR / 'nav.json')
    footer = load_json(COMPONENTS_DIR / 'footer.json')
    social = load_json(COMPONENTS_DIR / 'social.json')
    community = load_json(COMPONENTS_DIR / 'community.json')
    return {'nav': nav, 'footer': footer, 'social': social, 'community': community}


def load_articles_index():
    """Load articles index if it exists."""
    path = BASE_DIR / 'data' / 'articles.json'
    if path.exists():
        return load_json(path)
    return []


def load_features_data():
    """Load features page data (EN + per-language translations)."""
    data_dir = BASE_DIR / 'data'
    features = {}

    # EN
    en_path = data_dir / 'features.json'
    if en_path.exists():
        features['en'] = load_json(en_path)
    else:
        print(f"  WARNING: Missing features data: {en_path}")
        features['en'] = {}

    # Translations
    features_dir = data_dir / 'features'
    if features_dir.exists():
        for f in features_dir.iterdir():
            if f.suffix == '.json':
                lang = f.stem
                features[lang] = load_json(f)

    return features



# === HTML Sanitizer ===

_ALLOWED_TAGS = {
    'p','br','strong','b','em','i','u','a','ul','ol','li','h2','h3','h4','blockquote','code','pre',
    'table','thead','tbody','tr','th','td','img','figure','figcaption','hr','span','div'
}
_ALLOWED_ATTRS = {
    'a': {'href','title','target','rel','class','id'},
    'img': {'src','alt','title','loading','class','width','height'},
    'h2': {'id','class'}, 'h3': {'id','class'}, 'h4': {'id','class'},
    'span': {'class'}, 'div': {'class'}, 'table': {'class'}, 'th': {'scope','class'}, 'td': {'class'},
    'code': {'class'}, 'pre': {'class'}, 'blockquote': {'class'},
}

def sanitize_article_html(html):
    """Small allow-list sanitizer for trusted local article HTML.

    It removes script/style/iframe/object/embed blocks, event handlers, javascript: URLs,
    and tags outside the article allow-list. This keeps article_content usable with |safe
    without leaving raw executable HTML in JSON data.
    """
    if not html:
        return ''
    html = re.sub(r'<\s*(script|style|iframe|object|embed)\b[^>]*>.*?<\s*/\s*\1\s*>', '', html, flags=re.I|re.S)
    html = re.sub(r'\s+on[a-zA-Z]+\s*=\s*("[^"]*"|\'[^\']*\'|[^\s>]+)', '', html)
    def clean_tag(match):
        slash, tag, attrs = match.group(1), match.group(2).lower(), match.group(3) or ''
        if tag not in _ALLOWED_TAGS:
            return ''
        if slash:
            return f'</{tag}>'
        allowed = _ALLOWED_ATTRS.get(tag, set())
        cleaned=[]
        for am in re.finditer(r'([:\w-]+)\s*=\s*("[^"]*"|\'[^\']*\'|[^\s>]+)', attrs):
            name=am.group(1).lower()
            if name not in allowed:
                continue
            val=am.group(2)
            raw=val.strip('"\'').strip().lower()
            if name in {'href','src'} and (raw.startswith('javascript:') or raw.startswith('data:text/html')):
                continue
            cleaned.append(f'{name}={val}')
        return '<'+tag+((' '+' '.join(cleaned)) if cleaned else '')+'>'
    return re.sub(r'<\s*(/)?\s*([a-zA-Z0-9:-]+)([^>]*)>', clean_tag, html)

# === Build helpers ===

def compute_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def load_hashes():
    if HASHES_FILE.exists():
        return load_json(HASHES_FILE)
    return {}


def save_hashes(hashes):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with open(HASHES_FILE, 'w') as f:
        json.dump(hashes, f, indent=2)


def build_hreflang(lang, page_type, articles_index_all=None):
    """Generate hreflang data for a page."""
    hreflangs = []
    for code, info in LANGUAGES.items():
        # For article pages, only include languages where the article exists
        if articles_index_all and page_type not in PAGES:
            article_exists = any(a['slug'] == page_type and a['lang'] == code for a in articles_index_all)
            if not article_exists:
                continue
        if code == 'en':
            url = f'{SITE_URL}/{page_type}.html'
        else:
            url = f'{SITE_URL}/{code}/{page_type}.html'
        hreflangs.append({'code': info['hreflang'], 'url': url})
    return hreflangs


def build_canonical_url(lang, page_type):
    if lang == 'en':
        return f'{SITE_URL}/' if page_type == "index" else f'{SITE_URL}/{page_type}.html'
    else:
        return f'{SITE_URL}/{lang}/' if page_type == "index" else f'{SITE_URL}/{lang}/{page_type}.html'


def build_x_default_url(page_type):
    return f'{SITE_URL}/' if page_type == "index" else f'{SITE_URL}/{page_type}.html'


def build_lang_prefix(lang):
    if lang == 'en':
        return ''
    return f'/{lang}'



def build_language_options(page_type, current_lang='en', articles_index_all=None):
    """Build language switcher options for the same page when possible."""
    options = []
    for code, info in LANGUAGES.items():
        if page_type == 'author':
            href = f'{SITE_URL}/author/dean.html' if code == 'en' else f'{SITE_URL}/{code}/author/dean.html'
        elif page_type == '404':
            href = f'{SITE_URL}/404.html' if code == 'en' else f'{SITE_URL}/{code}/404.html'
        elif page_type in PAGES:
            href = build_canonical_url(code, page_type)
        elif articles_index_all and any(a.get('slug') == page_type and a.get('lang') == code for a in articles_index_all):
            href = f'{SITE_URL}/{page_type}.html' if code == 'en' else f'{SITE_URL}/{code}/{page_type}.html'
        else:
            href = build_canonical_url(code, 'resources')
        options.append({'code': code, 'name': info['native'], 'href': href})
    return options


def build_page_path(lang, page_type):
    if lang == 'en':
        return OUTPUT_DIR / f'{page_type}.html'
    else:
        return OUTPUT_DIR / lang / f'{page_type}.html'


# === Renderer ===

def render_page(env, page_type, lang, t, components, articles_index, articles_index_all=None, features_data=None, force=False):
    """Render a single page. Returns (path, skipped: bool)."""
    page_path = build_page_path(lang, page_type)

    # Compute content hash
    hash_input = f"{lang}:{page_type}:{json.dumps(t, sort_keys=True)}:{json.dumps(components, sort_keys=True)}"
    new_hash = compute_hash(hash_input)

    # Check cache
    if not force:
        hashes = load_hashes()
        cache_key = f'{lang}/{page_type}'
        if hashes.get(cache_key) == new_hash:
            return page_path, True  # Skipped

    # Prepare template context
    lang_info = LANGUAGES[lang]
    nav_links = components['nav']['links']
    languages = components['nav']['languages']

    # Mark current page in nav
    for link in nav_links:
        link['is_current'] = (link['href'] == f'/{page_type}.html' or
                              (page_type == 'index' and link['href'] == '/'))

    featured_articles = [a for a in articles_index if a.get('lang') == lang][:12]
    if lang == 'en':
        featured_slugs = [
            'tasker-alternative-voice-automation',
            'xiaomi-ai-ecosystem-2026',
            'voice-control-visually-impaired',
            'gemini-intelligence-supported-devices',
            'miclaw-vs-foneclaw',
            'wwdc-2026-ai-do-over-phone-agent',
            'agentic-ai-phone-explained',
            'gemini-vs-foneclaw',
            'android-vs-ios-26-5-voice-control',
            'voice-control-whatsapp',
            'gemini-intelligence-vs-siri',
            'foneclaw-vs-apple-intelligence',
        ]
        by_slug = {a.get('slug'): a for a in articles_index if a.get('lang') == 'en'}
        live_card_meta = {
            'tasker-alternative-voice-automation': {'title': 'Tasker Alternative: Android Voice Automation', 'category': 'Setup', 'description': 'No-code voice automation for Android without root access.', 'reading_time': '6 min'},
            'xiaomi-ai-ecosystem-2026': {'title': 'Xiaomi HyperOS AI Capabilities 2026', 'category': 'Industry', 'description': 'MiMo model, HyperOS integration, and the Xiaomi app ecosystem.', 'reading_time': '9 min'},
            'voice-control-visually-impaired': {'title': 'Voice Activated Phone for Blind Users', 'category': 'Use Cases', 'description': '100% voice control for accessibility — Voice Access, TalkBack, and more.', 'reading_time': '9 min'},
            'gemini-intelligence-supported-devices': {'title': 'Gemini Intelligence Supported Devices List 2026', 'category': 'Industry', 'description': 'Which phones support Gemini Intelligence and what you need.', 'reading_time': '10 min'},
            'miclaw-vs-foneclaw': {'title': 'Xiaomi MiClaw vs FoneClaw Phone Agent', 'category': 'Comparison', 'description': 'Closed beta vs open Android — MiClaw, MiMo, and HyperOS lock-in.', 'reading_time': '7 min'},
            'wwdc-2026-ai-do-over-phone-agent': {'title': 'WWDC 2026 Siri AI and Apple Intelligence', 'category': 'Industry', 'description': 'What Apple announced and what it means for phone agents.', 'reading_time': '7 min'},
            'agentic-ai-phone-explained': {'title': 'Agentic AI Phone: MiClaw, Gemini, Siri AI', 'category': 'Industry', 'description': 'What agentic AI means for your phone in 2026.', 'reading_time': '8 min'},
            'gemini-vs-foneclaw': {'title': 'Gemini Intelligence vs FoneClaw', 'category': 'Comparison', 'description': 'Can Gemini Intelligence control Android apps like FoneClaw?', 'reading_time': '6 min'},
            'android-vs-ios-26-5-voice-control': {'title': 'Android vs iOS: Voice Control Compared 2026', 'category': 'Comparison', 'description': 'Voice assistant integration across platforms — who wins?', 'reading_time': '6 min'},
            'voice-control-whatsapp': {'title': 'WhatsApp Voice Control: Hands-Free Guide 2026', 'category': 'Apps', 'description': 'Send messages, make calls, and manage chats with voice.', 'reading_time': '7 min'},
            'gemini-intelligence-vs-siri': {'title': 'Gemini Intelligence vs Siri AI: 2026 Comparison', 'category': 'Comparison', 'description': 'WWDC 2026, Gemini-powered Siri, and what it means for Android.', 'reading_time': '20 min'},
            'foneclaw-vs-apple-intelligence': {'title': 'FoneClaw vs Apple Intelligence', 'category': 'Comparison', 'description': 'Siri AI vs Android agent — App Intents vs cross-app control.', 'reading_time': '12 min'},
        }
        ordered = []
        for s in featured_slugs:
            if s in by_slug:
                card = dict(by_slug[s])
                card.update(live_card_meta.get(s, {}))
                ordered.append(card)
        if len(ordered) == len(featured_slugs):
            featured_articles = ordered

    context = {
        'lang': lang,
        'page_type': page_type,
        'lang_prefix': build_lang_prefix(lang),
        't': t,
        'canonical_url': build_canonical_url(lang, page_type),
        'x_default_url': build_x_default_url(page_type),
        'hreflang': build_hreflang(lang, page_type, articles_index_all),
        'nav': components['nav'],
        'footer': components['footer'],
        'languages': build_language_options(page_type, lang, articles_index_all),
        'articles': articles_index,
        'articles_index_all': articles_index_all,
        'community_cards': components['community']['cards'],
        'featured_articles': featured_articles,
        'lang_info': lang_info,
        'system_requirements': [
            'Android 9.0 or higher',
            '3GB RAM minimum',
            '100MB storage space',
            'Microphone permission',
            'Accessibility Service access',
        ],
        'download_faq': [
            {'question': 'Is FoneClaw really free?', 'answer': 'Yes. Core features are free. We may offer a Pro plan with advanced features later, but the core voice agent, basic automation, and system controls will always be free.'},
            {'question': 'Does it work on all Android phones?', 'answer': 'FoneClaw requires Android 9 or higher with at least 3GB of RAM. It works on most modern Android devices including Samsung, Google Pixel, OnePlus, and Xiaomi phones.'},
            {'question': 'Is my data safe?', 'answer': 'Yes. FoneClaw processes everything locally on your device. Your voice commands, contacts, and personal data never leave your phone unless you explicitly enable cloud sync.'},
            {'question': 'When will it be available?', 'answer': 'FoneClaw is available as an Android APK. Use the Download APK button above to get the latest available version.'},
        ],
    }

    # Add features data if available
    if features_data and page_type == 'features':
        feat = features_data.get(lang, features_data.get('en', {}))
        context['feature_categories'] = feat.get('feature_categories', [])
        context['demo_commands'] = feat.get('demo_commands', [])
        context['showcase_features'] = feat.get('showcase_features', [])
        context['trust_items'] = feat.get('trust_items', [])
        context['features_faq'] = feat.get('features_faq', [])

    # Render
    if page_type == "resources" and lang == "en":
        template_name = "resources-en.html"
    else:
        template_name = f"{page_type}.html"
    try:
        template = env.get_template(template_name)
        html = template.render(**context)
    except Exception as e:
        print(f"  ERROR rendering {lang}/{page_type}: {e}")
        return page_path, False

    # Write output
    page_path.parent.mkdir(parents=True, exist_ok=True)
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Update hash
    hashes = load_hashes()
    hashes[f'{lang}/{page_type}'] = new_hash
    save_hashes(hashes)

    return page_path, False


# === Sitemap ===

def generate_sitemap(output_dir, articles_index_all):
    """Generate sitemap.xml."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">')

    for lang in LANGUAGES:
        for page in PAGES:
            if lang == 'en':
                url = f'{SITE_URL}/' if page == 'index' else f'{SITE_URL}/{page}.html'
            else:
                url = f'{SITE_URL}/{lang}/{page}.html'

            lines.append('  <url>')
            lines.append(f'    <loc>{url}</loc>')
            lines.append(f'    <changefreq>weekly</changefreq>')
            lines.append(f'    <priority>0.8</priority>')

            # hreflang alternates
            for alt_lang, info in LANGUAGES.items():
                if alt_lang == 'en':
                    alt_url = f'{SITE_URL}/' if page == 'index' else f'{SITE_URL}/{page}.html'
                else:
                    alt_url = f'{SITE_URL}/{alt_lang}/{page}.html'
                lines.append(f'    <xhtml:link rel="alternate" hreflang="{info["hreflang"]}" href="{alt_url}"/>')

            # x-default
            lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{build_x_default_url(page)}"/>')
            lines.append('  </url>')

    # Add article URLs
    for a in articles_index_all:
        a_lang = a.get('lang', 'en')
        a_slug = a.get('slug', '')
        if a_lang == 'en':
            a_url = f'{SITE_URL}/{a_slug}.html'
        else:
            a_url = f'{SITE_URL}/{a_lang}/{a_slug}.html'
        lines.append('  <url>')
        lines.append(f'    <loc>{a_url}</loc>')
        lines.append(f'    <changefreq>monthly</changefreq>')
        lines.append(f'    <priority>0.6</priority>')
        lines.append('  </url>')

    # Add hub page URLs
    for slug in HUB_PAGES:
        h_url = f'{SITE_URL}/{slug}/index.html'
        lines.append('  <url>')
        lines.append(f'    <loc>{h_url}</loc>')
        lines.append(f'    <changefreq>weekly</changefreq>')
        lines.append(f'    <priority>0.7</priority>')
        lines.append('  </url>')

    # Add sub-hub page URLs
    for parent, slugs in SUB_HUB_PAGES.items():
        for slug in slugs:
            sh_url = f'{SITE_URL}/{parent}/{slug}/index.html'
            lines.append('  <url>')
            lines.append(f'    <loc>{sh_url}</loc>')
            lines.append(f'    <changefreq>weekly</changefreq>')
            lines.append(f'    <priority>0.6</priority>')
            lines.append('  </url>')

    lines.append('</urlset>')

    sitemap_path = output_dir / 'sitemap.xml'
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    return sitemap_path


# === Main ===

# === Article Rendering ===

def load_article(lang, slug):
    """Load a single article JSON file."""
    path = ARTICLES_DIR / lang / f'{slug}.json'
    if path.exists():
        return load_json(path)
    return None


def render_article(env, lang, slug, article_data, t, components, articles_index, articles_index_all=None, force=False):
    """Render a single article page."""
    if lang == 'en':
        page_path = OUTPUT_DIR / f'{slug}.html'
    else:
        page_path = OUTPUT_DIR / lang / f'{slug}.html'

    # Hash check
    hash_input = f"article:{lang}:{slug}:{json.dumps(article_data, sort_keys=True, ensure_ascii=False)}"
    new_hash = compute_hash(hash_input)
    hashes = load_hashes()
    cache_key = f'{lang}/article/{slug}'
    if hashes.get(cache_key) == new_hash and not force:
        return page_path, True

    # Prepare context
    lang_info = LANGUAGES[lang]
    nav_links = components['nav']['links']
    languages = components['nav']['languages']
    for link in nav_links:
        link['is_current'] = (link['key'] == 'resources')

    # Normalize article metadata for templates and JSON-LD.
    # Older article JSON files often have `date` but not `date_display`,
    # `date_published`, `date_modified`, or author fields.
    article_data = dict(article_data)
    article_date = article_data.get('date') or article_data.get('date_published') or ''
    article_data.setdefault('date_display', article_date)
    article_data.setdefault('date_published', article_date)
    article_data.setdefault('date_modified', article_date)
    article_data.setdefault('author', 'Dean')
    article_data.setdefault('author_slug', 'dean')

    # Get related articles data
    related = []
    for rel_slug in article_data.get('related', []):
        rel = load_article(lang, rel_slug)
        if rel:
            related.append({
                'slug': rel_slug,
                'title': rel.get('title', ''),
                'category': rel.get('category', ''),
                'reading_time': rel.get('reading_time', ''),
                'image': rel.get('image', ''),
                'description': rel.get('description', '')
            })

    context = {
        'lang': lang,
        'lang_prefix': build_lang_prefix(lang),
        't': t,
        'canonical_url': f'{SITE_URL}/{lang}/{slug}.html' if lang != 'en' else f'{SITE_URL}/{slug}.html',
        'x_default_url': f'{SITE_URL}/{slug}.html',
        'hreflang': build_hreflang(lang, slug, articles_index_all),
        'nav': components['nav'],
        'footer': components['footer'],
        'languages': build_language_options(slug, lang, articles_index_all),
        'articles': articles_index,
        'articles_index_all': articles_index_all,
        'lang_info': lang_info,
        'page_type': 'article',
        # Article-specific
        'article': article_data,
        'article_content': sanitize_article_html(article_data.get('body_html', '')),
        'article_title': article_data.get('title', ''),
        'article_description': article_data.get('description', ''),
        'article_category': article_data.get('category', ''),
        'article_reading_time': article_data.get('reading_time', ''),
        'article_image': article_data.get('image', ''),
        'og_image': f"{SITE_URL}/images/articles/{article_data.get('image', '')}" if article_data.get('image') else f"{SITE_URL}/images/og-homepage.jpg",
        'article_faq': article_data.get('faq', []),
        'article_related': related,
        'related_articles': related,
        'articles_index_all': articles_index_all,
        'article_slug': slug,
    }

    try:
        template = env.get_template('article.html')
        html = template.render(**context)
    except Exception as e:
        print(f"  ERROR rendering {lang}/article/{slug}: {e}")
        return page_path, False

    page_path.parent.mkdir(parents=True, exist_ok=True)
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(html)

    hashes[cache_key] = new_hash
    save_hashes(hashes)
    return page_path, False

def main():
    parser = argparse.ArgumentParser(description='FoneClaw v3 Builder')
    parser.add_argument('--lang', help='Build only one language (e.g., zh)')
    parser.add_argument('--page', help='Build only one page type (e.g., features)')
    parser.add_argument('--force', action='store_true', help='Force full rebuild')
    parser.add_argument('--dry-run', action='store_true', help='Preview without building')
    args = parser.parse_args()

    start_time = time.time()

    # Load data
    print("Loading translations...")
    translations = load_translations()
    print(f"  Loaded {len(translations)} languages")

    print("Loading components...")
    components = load_components()
    print(f"  Loaded nav/footer/social")

    print("Loading articles index...")
    articles_index_all = load_articles_index()
    print(f"  Loaded {len(articles_index_all)} articles")

    print("Loading features data...")
    features_data = load_features_data()
    print(f"  Loaded features for {len(features_data)} languages")

    # Setup Jinja2
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(['html', 'xml'])
    )

    # Determine languages to build
    if args.lang:
        if args.lang not in LANGUAGES:
            print(f"ERROR: Unknown language '{args.lang}'. Available: {', '.join(LANGUAGES.keys())}")
            sys.exit(1)
        build_langs = [args.lang]
    else:
        build_langs = list(LANGUAGES.keys())

    # Determine pages to build
    if args.page:
        if args.page not in PAGES:
            print(f"ERROR: Unknown page '{args.page}'. Available: {', '.join(PAGES)}")
            sys.exit(1)
        build_pages = [args.page]
    else:
        build_pages = PAGES

    # Build
    total = len(build_langs) * len(build_pages)
    built = 0
    skipped = 0
    errors = 0

    print(f"\nBuilding {total} pages ({len(build_langs)} languages × {len(build_pages)} pages)...")
    if args.force:
        print("  Mode: FORCE (rebuild all)")
    elif args.dry_run:
        print("  Mode: DRY RUN (no files written)")

    for lang in build_langs:
        articles_index = sorted([a for a in articles_index_all if a.get('lang') == lang], key=lambda x: x.get('date', '2026-01-01'), reverse=True)
        t = translations.get(lang, translations.get('en', {}))
        for page in build_pages:
            if args.dry_run:
                # Check hash without rendering
                hashes = load_hashes()
                cache_key = f'{lang}/{page}'
                hash_input = f"{lang}:{page}:{json.dumps(t, sort_keys=True)}"
                new_hash = compute_hash(hash_input)
                if hashes.get(cache_key) == new_hash and not args.force:
                    skipped += 1
                else:
                    built += 1
                    print(f"  WOULD BUILD: {lang}/{page}")
            else:
                page_path, was_skipped = render_page(
                    env, page, lang, t, components, articles_index, articles_index_all, features_data=features_data,
                    force=args.force
                )
                if was_skipped:
                    skipped += 1
                else:
                    built += 1
                    rel_path = page_path.relative_to(BASE_DIR)
                    print(f"  BUILT: {rel_path}")

    # Build articles
    print(f"\nBuilding articles...")
    for lang in build_langs:
        articles_index = [a for a in articles_index_all if a.get("lang") == lang]
        article_slugs = list(set(a["slug"] for a in articles_index))
        for slug in article_slugs:
            article_data = load_article(lang, slug)
            if not article_data:
                continue
            if args.dry_run:
                built += 1
                print(f"  WOULD BUILD: {lang}/{slug}.html")
            else:
                page_path, was_skipped = render_article(
                    env, lang, slug, article_data, translations.get(lang, translations.get("en", {})),
                    components, articles_index, articles_index_all, force=args.force
                )
                if was_skipped:
                    skipped += 1
                else:
                    built += 1
                    rel_path = page_path.relative_to(BASE_DIR)
                    print(f"  BUILT: {rel_path}")

    # Build 404 pages (all languages, noindex, excluded from sitemap)
    print("\nBuilding 404 pages...")
    try:
        template = env.get_template('404.html')
        for lang in LANGUAGES:
            t_lang = translations.get(lang, translations.get('en', {}))
            nav_links = copy.deepcopy(components['nav']['links'])
            for link in nav_links:
                link['is_current'] = False
            lang_prefix = build_lang_prefix(lang)
            canonical = f'{SITE_URL}/404.html' if lang == 'en' else f'{SITE_URL}/{lang}/404.html'
            ctx = {
                'lang': lang,
                'lang_prefix': lang_prefix,
                't': t_lang,
                'canonical_url': canonical,
                'x_default_url': f'{SITE_URL}/404.html',
                'robots_meta': 'noindex, nofollow',
                'hreflang': [{'code': info['hreflang'], 'url': f'{SITE_URL}/404.html' if l == 'en' else f'{SITE_URL}/{l}/404.html'} for l, info in LANGUAGES.items()],
                'nav': {'links': nav_links, 'languages': components['nav']['languages']},
                'footer': components['footer'],
                'languages': build_language_options('404', lang),
                'articles': [],
                'lang_info': LANGUAGES[lang],
                'page_type': '404',
            }
            html = template.render(**ctx)
            page_path = OUTPUT_DIR / '404.html' if lang == 'en' else OUTPUT_DIR / lang / '404.html'
            page_path.parent.mkdir(parents=True, exist_ok=True)
            page_path.write_text(html, encoding='utf-8')
            built += 1
            print(f"  BUILT: {page_path.relative_to(OUTPUT_DIR)}")
    except Exception as e:
        print(f'  ERROR rendering 404: {e}')

    # Build author pages (all languages)
    print("\nBuilding author pages...")
    template = env.get_template('author/dean.html')
    for lang in LANGUAGES:
        try:
            lang_articles = sorted(
                [a for a in articles_index_all if a.get('lang') == lang],
                key=lambda x: x.get('date', ''), reverse=True
            )
            categories = sorted(set(a.get('category', '') for a in lang_articles if a.get('category')))
            t_lang = translations.get(lang, translations.get('en', {}))
            lang_info = LANGUAGES[lang]
            lang_prefix = build_lang_prefix(lang)
            canonical = f'{SITE_URL}/author/dean.html' if lang == 'en' else f'{SITE_URL}/{lang}/author/dean.html'
            author_ctx = {
                'lang': lang,
                'lang_prefix': lang_prefix,
                't': t_lang,
                'canonical_url': canonical,
                'x_default_url': f'{SITE_URL}/author/dean.html',
                'hreflang': [{'code': info['hreflang'], 'url': f'{SITE_URL}/author/dean.html' if l == 'en' else f'{SITE_URL}/{l}/author/dean.html'} for l, info in LANGUAGES.items() if any(a.get('lang') == l for a in articles_index_all)],
                'nav': components['nav'],
                'footer': components['footer'],
                'languages': build_language_options('author', lang),
                'articles': lang_articles,
                'articles_index_all': articles_index_all,
                'lang_info': lang_info,
                'page_type': 'author',
                'author_articles': lang_articles,
                'article_count': len(lang_articles),
                'category_count': len(categories),
            }
            html = template.render(**author_ctx)
            if lang == 'en':
                out_path = OUTPUT_DIR / 'author' / 'dean.html'
            else:
                out_path = OUTPUT_DIR / lang / 'author' / 'dean.html'
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)
            built += 1
            print(f"  BUILT: {lang}/author/dean.html ({len(lang_articles)} articles)")
        except Exception as e:
            print(f"  ERROR rendering author/{lang}: {e}")
            errors += 1

    # Build hub pages (EN only)
    print(f"\nBuilding hub pages...")
    for slug in HUB_PAGES:
        hub_path = OUTPUT_DIR / slug / 'index.html'
        template_name = f'hub-{slug}.html'
        try:
            template = env.get_template(template_name)
            # Create minimal context
            hub_context = {
                'lang': 'en',
                'lang_prefix': '',
                't': translations.get('en', {}),
                'canonical_url': f'{SITE_URL}/{slug}/index.html',
                'x_default_url': f'{SITE_URL}/{slug}/index.html',
                'hreflang': [{'code': 'en', 'url': f'{SITE_URL}/{slug}/index.html'}],
                'nav': components['nav'],
                'footer': components['footer'],
                'languages': components['nav']['languages'],
                'articles': articles_index_all,
                'lang_info': {'hreflang': 'en', 'dir': ''},
                'page_type': f'hub-{slug}',
            }
            html = template.render(**hub_context)
            hub_path.parent.mkdir(parents=True, exist_ok=True)
            with open(hub_path, 'w', encoding='utf-8') as f:
                f.write(html)
            built += 1
            print(f"  BUILT: {slug}/index.html")
        except Exception as e:
            print(f"  ERROR rendering hub-{slug}: {e}")
            errors += 1

    # Build sub-hub pages (EN only)
    for parent, slugs in SUB_HUB_PAGES.items():
        for slug in slugs:
            subhub_path = OUTPUT_DIR / parent / slug / 'index.html'
            template_name = f'hub-{parent}-{slug}.html'
            try:
                template = env.get_template(template_name)
                subhub_context = {
                    'lang': 'en',
                    'lang_prefix': '',
                    't': translations.get('en', {}),
                    'canonical_url': f'{SITE_URL}/{parent}/{slug}/index.html',
                    'x_default_url': f'{SITE_URL}/{parent}/{slug}/index.html',
                    'hreflang': [{'code': 'en', 'url': f'{SITE_URL}/{parent}/{slug}/index.html'}],
                    'nav': components['nav'],
                    'footer': components['footer'],
                    'languages': components['nav']['languages'],
                    'articles': articles_index_all,
                    'lang_info': {'hreflang': 'en', 'dir': ''},
                    'page_type': f'hub-{parent}-{slug}',
                }
                html = template.render(**subhub_context)
                subhub_path.parent.mkdir(parents=True, exist_ok=True)
                with open(subhub_path, 'w', encoding='utf-8') as f:
                    f.write(html)
                built += 1
                print(f"  BUILT: {parent}/{slug}/index.html")
            except Exception as e:
                print(f"  ERROR rendering hub-{parent}-{slug}: {e}")
                errors += 1

    # Generate sitemap
    if not args.dry_run:
        print("\nGenerating sitemap...")
        sitemap_path = generate_sitemap(OUTPUT_DIR, articles_index_all)
        print(f"  Written: {sitemap_path.relative_to(BASE_DIR)}")
        robots_path = OUTPUT_DIR / 'robots.txt'
        robots_path.write_text(f"User-agent: *\nAllow: /\nDisallow: /404.html\nSitemap: {SITE_URL}/sitemap.xml\n", encoding='utf-8')
        print(f"  Written: {robots_path.relative_to(BASE_DIR)}")

    elapsed = time.time() - start_time
    print(f"\nDone in {elapsed:.1f}s: {built} built, {skipped} skipped, {errors} errors")


if __name__ == '__main__':
    main()
