# Shared HTML components for all FoneClaw pages
# Used by build_multi.py and standalone page generators

import os

base = '/home/administrator/clawfone-v2'

with open(os.path.join(base, '_style.css')) as f:
    _CSS = f.read()

_CSS += """
#download-btn.available {
    background: linear-gradient(135deg,#3fb950,#2ea043);
    pointer-events: auto;
    opacity: 1;
    box-shadow: 0 4px 16px rgba(63,185,80,.3);
}
#download-btn.unavailable {
    background: #5a1d1d;
    pointer-events: none;
    opacity: 0.6;
}
"""


# Nav items: (index, label, href)
from _social_share import social_share

NAV_ITEMS = [
    (0, 'Home', '/'),
    (1, 'Features', '/features.html'),
    (2, 'Download', '/download.html'),
    (3, 'Resources', '/resources.html'),
    (4, 'Community', '/community.html'),
]

def head(title, description, canonical_path, extra_css='', og_image='https://www.foneclaw.ai/og-image.png', lang='en', hreflang_tags=''):
    favicon = '<link rel="icon" type="image/png" href="/favicon.png">'
    return f'''<!DOCTYPE html>
<html lang="{lang}"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.foneclaw.ai{canonical_path}">
{hreflang_tags}
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://www.foneclaw.ai{canonical_path}">
<meta property="og:image" content="{og_image}">
<meta property="og:site_name" content="FoneClaw">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
<meta name="theme-color" content="#080c18">
{favicon}
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/css/foneclaw-apk-cta.css">
<script defer src="/assets/js/foneclaw-apk-cta.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/_style.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0PHX8QGTBF"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-0PHX8QGTBF');</script>
<script>
// GA4 Event Tracking Utilities
function trackEvent(eventName, params){{gtag('event', eventName, params || {{}});}}
function trackShare(platform, articleSlug){{trackEvent('share',{{method:platform,content_type:'article',item_id:articleSlug}});}}
function trackScroll(depth, articleSlug){{trackEvent('scroll_depth',{{percent:depth,article:articleSlug}});}}
function trackOutbound(url, articleSlug){{trackEvent('outbound_click',{{link_url:url,article:articleSlug}});}}
function trackFAQ(question, articleSlug){{trackEvent('faq_expand',{{question:question,article:articleSlug}});}}
</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"FoneClaw","applicationCategory":"UtilitiesApplication","operatingSystem":"Android","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}</script>
{_CSS}
</style>
{extra_css}
</head><body>'''


NAV_ITEMS_ZH = [
    (0, '首页', '/'),
    (1, '功能', '/features.html'),
    (2, '下载', '/download.html'),
    (3, '资源', '/resources.html'),
    (4, '社区', '/community.html'),
]

NAV_ITEMS_TW = [
    (0, '首頁', '/'),
    (1, '功能', '/features.html'),
    (2, '下載', '/download.html'),
    (3, '資源', '/resources.html'),
    (4, '社群', '/community.html'),
]

LANG_DIR = {'en': '', 'zh': 'zh', 'tw': 'tw'}
LANG_OPTIONS = [('en', 'English'), ('zh', '简体中文'), ('tw', '繁體中文')]

def lang_prefix(lang='en'):
    d = LANG_DIR.get(lang, '')
    return f'/{d}' if d else ''

def nav(active_page=-1, lang='en', canonical_path=''):
    logo = '<img src="/favicon.png" alt="FoneClaw">'
    prefix = lang_prefix(lang)
    links = ''
    items = NAV_ITEMS_TW if lang == 'tw' else (NAV_ITEMS_ZH if lang == 'zh' else NAV_ITEMS)
    for idx, label, href in items:
        cls = ' class="on"' if idx == active_page else ''
        links += f'<a{cls} href="{prefix}{href}">{label}</a>'
    # Language dropdown selector — use full absolute URLs to avoid CDN caching issues
    page_map = {
        'en': {'index': 'https://www.foneclaw.ai/index.html', 'features': 'https://www.foneclaw.ai/features.html', 'download': 'https://www.foneclaw.ai/download.html', 'resources': 'https://www.foneclaw.ai/resources.html', 'community': 'https://www.foneclaw.ai/community.html'},
        'zh': {'index': 'https://www.foneclaw.ai/zh/index.html', 'features': 'https://www.foneclaw.ai/zh/features.html', 'download': 'https://www.foneclaw.ai/zh/download.html', 'resources': 'https://www.foneclaw.ai/zh/resources.html', 'community': 'https://www.foneclaw.ai/zh/community.html'},
        'tw': {'index': 'https://www.foneclaw.ai/tw/index.html', 'features': 'https://www.foneclaw.ai/tw/features.html', 'download': 'https://www.foneclaw.ai/tw/download.html', 'resources': 'https://www.foneclaw.ai/tw/resources.html', 'community': 'https://www.foneclaw.ai/tw/community.html'},
    }
    # Determine current page name from active_page index
    page_names = ['index', 'features', 'download', 'resources', 'community']
    current_page = page_names[active_page] if 0 <= active_page < len(page_names) else None
    lang_options = []
    for code, label in LANG_OPTIONS:
        if current_page and current_page in page_map.get(code, {}):
            url = page_map[code][current_page]
        else:
            # For article pages or unknown pages, construct URL from current path
            import os
            current_filename = os.path.basename(canonical_path) if canonical_path else 'index.html'
            if not current_filename.endswith('.html'):
                current_filename = 'index.html'
            url = f'https://www.foneclaw.ai/{code}/{current_filename}' if code != 'en' else f'https://www.foneclaw.ai/{current_filename}'
        sel = ' selected' if code == lang else ''
        lang_options.append(f'<option value="{url}"{sel}>{label}</option>')
    lang_switcher = f'<select class="lang-sel" onchange="window.location.href=this.value">{chr(10).join(lang_options)}</select>'
    logo_href = f'{prefix}/'
    return f'<nav class="top-nav" aria-label="Main navigation"><div class="nb"><a class="logo" href="{logo_href}">{logo}FoneClaw</a><button class="hamburger" onclick="this.nextElementSibling.classList.toggle(\'open\')" aria-label="Menu">\u2630</button><div class="nr">{links}{lang_switcher}</div></div></nav>'

def footer(lang='en'):
    logo = '<img src="/favicon.png" alt="FoneClaw">'
    if lang == 'tw':
        slogan = 'FoneClaw 是能幫你實際操作 Android 手機的 AI 助手，不只是語音助理。'
        ft_product = '產品'
        ft_topics = '主題'
        ft_company = '公司'
        ft_features = '功能'
        ft_download = '下載'
        ft_vc = '語音控制'
        ft_comp = '產品比較'
        ft_ai = 'AI Agent'
        ft_news = '產業新聞'
        ft_resources = '全部資源'
        ft_community = '社群'
        ft_privacy = '隱私權政策'
        ft_copy = '保留所有權利。'
    elif lang == 'zh':
        slogan = 'FoneClaw 是能帮你实际操作 Android 手机的 AI 助手，不仅仅是语音助手。'
        ft_product = '产品'
        ft_topics = '主题'
        ft_company = '公司'
        ft_features = '功能'
        ft_download = '下载'
        ft_vc = '语音控制'
        ft_comp = '产品对比'
        ft_ai = 'AI Agent'
        ft_news = '行业资讯'
        ft_resources = '全部资源'
        ft_community = '社区'
        ft_privacy = '隐私政策'
        ft_copy = '保留所有权利。'
    else:
        slogan = 'FoneClaw is the Android AI agent that actually controls your phone — not just answers questions.'
        ft_product = 'Product'
        ft_topics = 'Topics'
        ft_company = 'Company'
        ft_features = 'Features'
        ft_download = 'Download'
        ft_vc = 'Voice Control'
        ft_comp = 'Comparisons'
        ft_ai = 'AI Agent'
        ft_news = 'Industry News'
        ft_resources = 'All Resources'
        ft_community = 'Community'
        ft_privacy = 'Privacy Policy'
        ft_copy = 'All rights reserved.'
    prefix = lang_prefix(lang)
    if lang in ('zh', 'tw'):
        topics_links = f'<a href="{prefix}/resources.html">{ft_resources}</a>'
    else:
        topics_links = f'<a href="/voice-control/index.html">{ft_vc}</a><a href="/comparisons/index.html">{ft_comp}</a><a href="/ai-agent/index.html">{ft_ai}</a><a href="/news/index.html">{ft_news}</a><a href="{prefix}/resources.html">{ft_resources}</a>'
    return f'''<footer aria-label="Footer"><div class="wrap"><div class="ft-inner">
<div class="ft-col"><div class="logo" style="margin-bottom:12px">{logo}FoneClaw</div><p style="color:#8b949e;font-size:14px">{slogan}</p></div>
<div class="ft-col"><div class="ft-heading">{ft_product}</div><a href="{prefix}/features.html">{ft_features}</a><a href="{prefix}/download.html">{ft_download}</a></div>
<div class="ft-col"><div class="ft-heading">{ft_topics}</div>{topics_links}</div>
<div class="ft-col"><div class="ft-heading">{ft_company}</div><a href="{prefix}/community.html">{ft_community}</a><a href="/privacy.html">{ft_privacy}</a></div>
</div><p style="text-align:center;margin-top:30px;color:#484f58;font-size:12px">&copy; 2026 FoneClaw. {ft_copy}</p></div></footer>
<button class="back-to-top" id="backToTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>
</button>'''

def js(trans_json='{}'):
    return f"""<script>
function showArticle(id){{var el=document.getElementById("art-"+id);if(el){{el.classList.add("show");document.body.style.overflow="hidden";window.scrollTo(0,0);}}}}
function hideArticle(){{document.querySelectorAll(".article-overlay").forEach(function(e){{e.classList.remove("show");}});document.body.style.overflow="";}}
document.addEventListener("keydown",function(e){{if(e.key==="Escape")hideArticle();}});
window.addEventListener("scroll",function(){{var b=document.getElementById("backToTop");if(b){{if(window.scrollY>400){{b.style.opacity="1";b.style.visibility="visible";}}else{{b.style.opacity="0";b.style.visibility="hidden";}}}}}});
</script>
"""


def full_page(title, description, canonical_path, active_page, body_html, extra_css='', og_image='https://www.foneclaw.ai/og-image.png', lang='en', hreflang_tags=''):
    """Generate a complete page with head, nav, content, footer, back-to-top, js."""
    html = []
    html.append(head(title, description, canonical_path, extra_css, og_image, lang, hreflang_tags))
    html.append(nav(active_page, lang, canonical_path))
    html.append('<main>')
    html.append(body_html)
    html.append('</main>')
    html.append(footer(lang))
    html.append(social_share(lang=lang))
    html.append(js())
    html.append('</body></html>')
    return '\n'.join(html)
