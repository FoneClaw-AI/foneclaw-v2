#!/usr/bin/env python3
"""
Generate Traditional Chinese (tw) article pages for FoneClaw.

Creates Traditional Chinese (Taiwan) versions of articles linked from the homepage
and resources page. Currently translates UI chrome (nav, footer, breadcrumbs,
section labels) and meta data (title, description) to Chinese while keeping
article body text in English. Full body translation is a separate task.

Usage:
    python3 gen_tw_articles.py
"""

import os, sys, json, datetime, importlib.util, re

base = '/home/administrator/clawfone-v2'
sys.path.insert(0, base)
os.chdir(base)

# ── Load shared components ──────────────────────────────────────────
from _components import head, nav, footer, js, full_page, NAV_ITEMS
from _social_share import social_share

# ── Load article data (same as build_multi.py) ──────────────────────
def load_batch(fname):
    spec = importlib.util.spec_from_file_location("batch", os.path.join(base, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.BATCH

articles_data = []
batch_files = [
    # Original batches 1-10d
    *[f'articles_batch{i}.py' for i in range(1, 11)],
    'articles_batch10b.py', 'articles_batch10c.py', 'articles_batch10d.py',
    # Batches 11-13
    'articles_batch11.py', 'articles_batch12.py',
    'articles_batch131.py', 'articles_batch132.py', 'articles_batch133.py',
    # Batch 14 sub-batches
    *[f'articles_batch14{i}.py' for i in range(1, 6)],
    # Batch 15 sub-batches
    *[f'articles_batch15{i}.py' for i in range(1, 6)],
    # Special batches
    'articles_batch156.py',
    'articles_batch_xiaomi_lobster.py',
    'articles_batch_tencent_cost.py',
    'articles_batch_xiaomi_summit.py',
    'articles_batch_foneclaw_vs_likeclaw.py',
    'articles_batch_foneclaw_vs_apple_intelligence.py',
    'articles_batch_apple_intelligence_accessibility_foneclaw.py',
    'articles_batch_foneclaw_vs_samsung_galaxy_ai.py',
    'articles_batch_ai_phone_agent_harness.py',
    'articles_batch_mediatek_dimensity_phone_agent.py',
    'articles_batch_ios_27_siri_ai_agent.py',
    'articles_batch_ios27_gemini.py',
    'articles_batch_copilot_trends.py',
    'articles_batch_agent_spending.py',
    'articles_batch_gemini_intelligence_pixel_9_excluded.py',
    'articles_batch_gemini_intelligence_supported_devices.py',
    'articles_batch_samsung_galaxy_s26_ai_features_s25.py',
    'articles_batch_foneclaw_vs_openally.py',
    'articles_batch_foneclaw_vs_minimax.py',
    'articles_batch_foneclaw_vs_all_in_one_ai_agent.py',
    'articles_batch_foneclaw_vs_nebula_ai.py',
    'articles_batch_skyclaw_vs_foneclaw.py',
    'articles_batch_foneclaw_vs_adobe_firefly.py',
    'articles_batch_cloud_local.py',
    'articles_batch_superapp.py',
    'articles_batch_hymem.py',
    'articles_batch_workbuddy.py',
    'articles_batch_build.py',
    'articles_batch_nvidia.py',
    'articles_batch_glasses.py',
    'articles_batch_raybans.py',
    'articles_batch_discover.py',
    'articles_batch_trust.py',
    'articles_batch_enterprise.py',
    'articles_batch_token.py',
    'articles_batch_lab_to_pocket.py',
    'articles_batch_security.py',
    'articles_batch_spark.py',
    'articles_batch_wwdc.py',
    'articles_batch_context.py',
    'articles_batch_mcp.py',
    'articles_batch_apple_local.py',
    'articles_batch_app_intents.py',
    'articles_batch_ai_pro.py',
    'articles_batch_scout.py',
    'articles_batch_os_agent_foundation.py',
    'articles_batch_ai_chip_race.py',
    'articles_batch_self_improving.py',
    'articles_batch_eval_driven.py',
    'articles_batch_closed_loop.py',
    'articles_batch_llm_optimization.py',
    'articles_batch_os_agent_traffic.py',
    'articles_batch_openai_no_app.py',
    'articles_batch_dev_guide.py',
    'articles_batch_voice_first.py',
    'articles_batch_voice_control_hub.py',
    'articles_batch_miclaw_review.py',
    'batch_gemini-intelligence-form-filling.py',
    'batch_gemini-intelligence-widgets.py',
    'batch_ai_notification.py',
    'articles_batch_1000_tps_phone_agent.py',
    'articles_batch_jd_tencent_ai_agent.py',
    'articles_batch_wechat_ai_agent.py',
    'articles_batch_claude_code_multi_agent.py',
]

for bf in batch_files:
    try:
        articles_data.extend(load_batch(bf))
    except Exception:
        pass

# Normalize to 6 elements
articles_data = [item[:6] if len(item) >= 6 else item for item in articles_data]

# Deduplicate by slug (first occurrence wins)
seen_slugs = set()
deduped = []
for item in articles_data:
    if item[0] not in seen_slugs:
        seen_slugs.add(item[0])
        deduped.append(item)
articles_data = deduped

print(f"Loaded {len(articles_data)} articles")

# ── URL_MAP (same as build_multi.py) ────────────────────────────────
URL_MAP = {
    'howto_voice_android': '/voice-control-android',
    'howto_texts_handsfree': '/send-texts-hands-free',
    'howto_multistep': '/automate-multi-step-tasks',
    'howto_elderly_setup': '/voice-control-elderly',
    'howto_driving_voice': '/voice-commands-driving',
    'howto_smart_home': '/smart-home-voice-control',
    'uc_commuting': '/voice-control-commuters',
    'uc_seniors': '/ai-phone-seniors',
    'uc_cooking': '/hands-free-cooking',
    'uc_emergency': '/emergency-voice-commands',
    'uc_productivity': '/productivity-automation',
    'uc_visual_impaired': '/voice-control-visually-impaired',
    'uc_parenting': '/parenting-hands-free',
    'uc_fitness': '/voice-fitness',
    'comp_vs_siri': '/foneclaw-vs-siri',
    'comp_vs_google': '/foneclaw-vs-google-assistant',
    'comp_vs_alexa': '/foneclaw-vs-alexa',
    'comp_best_apps': '/best-voice-control-apps-2026',
    'comp_ai_replacing': '/ai-agents-replacing-assistants',
    'comp_vs_gemini': '/gemini-vs-foneclaw',
    'comp_vs_miclaw': '/miclaw-vs-foneclaw',
    'ai-agent-vs-traditional-apps': '/ai-agent-vs-traditional-apps',
    'tasker-alternative-voice-automation': '/tasker-alternative-voice-automation',
    'voice-assistant-privacy-security': '/voice-assistant-privacy-security',
    'voice-control-dirty-hands': '/voice-control-dirty-hands',
    'top-10-ai-agents-2026': '/top-10-ai-agents-2026',
    'hermes-agent-vs-openclaw-vs-foneclaw': '/hermes-agent-vs-openclaw-vs-foneclaw',
    'why-local-ai-agents-never-go-down': '/why-local-ai-agents-never-go-down',
    'automate-instagram-with-voice': '/automate-instagram-with-voice',
    'android-vs-ios-26-5-voice-control': '/android-vs-ios-26-5-voice-control',
    'control-samsung-smart-tv-voice': '/control-samsung-smart-tv-voice',
    'voice-control-wearables': '/voice-control-wearables',
    'small-businesses-use-ai-agents': '/small-businesses-use-ai-agents',
    'cerebras-future-ai-hardware': '/cerebras-future-ai-hardware',
    'trump-phone-mobile-ai': '/trump-phone-mobile-ai',
    'top-10-ai-agent-models-2026': '/top-10-ai-agent-models-2026',
    'ai-phone-war-2026': '/ai-phone-war-2026',
    'ai-terminal-war-agent-battlefield': '/ai-terminal-war-agent-battlefield',
    'xiaomi-ai-ecosystem-2026': '/xiaomi-ai-ecosystem-2026',
    'author/dean': '/author/dean',
    'voice-control-whatsapp': '/voice-control-whatsapp',
    'voice-control-youtube': '/voice-control-youtube',
    'voice-control-tiktok': '/voice-control-tiktok',
    'voice-control-facebook': '/voice-control-facebook',
    'voice-control-twitter': '/voice-control-twitter',
    'voice-control-telegram': '/voice-control-telegram',
    'voice-control-linkedin': '/voice-control-linkedin',
    'voice-control-snapchat': '/voice-control-snapchat',
    'voice-control-reddit': '/voice-control-reddit',
    'voice-control-discord': '/voice-control-discord',
    'claude-ai-login-android': '/claude-ai-login-android',
    'agentic-ai-phone-explained': '/agentic-ai-phone-explained',
    'perplexity-ai-vs-google-search': '/perplexity-ai-vs-google-search',
    'gemini-intelligence-complete-guide': '/gemini-intelligence-complete-guide',
    'gemini-intelligence-features': '/gemini-intelligence-features',
    'ai-agent-phone-control': '/ai-agent-phone-control',
    'xiaomi-miclaw-explained': '/xiaomi-miclaw-explained',
    'huawei-phone-agent': '/huawei-phone-agent',
    'gemini-intelligence-vs-siri': '/gemini-intelligence-vs-siri',
    'miclaw-vs-openclaw': '/miclaw-vs-openclaw',
    'gemini-intelligence-productivity': '/gemini-intelligence-productivity',
    'gemini-intelligence-voice-control': '/gemini-intelligence-voice-control',
    'how-to-install-miclaw': '/how-to-install-miclaw',
    'voice-control-pinterest': '/voice-control-pinterest',
    'xiaomi-lobster-phone-ai-features': '/xiaomi-lobster-phone-ai-features',
    'ai-notification-management': '/ai-notification-management',
    'gemini-intelligence-form-filling': '/gemini-intelligence-form-filling',
    'gemini-intelligence-widgets': '/gemini-intelligence-widgets',
    'gemini-intelligence-supported-devices': '/gemini-intelligence-supported-devices',
    'tencent-phone-agent-cost': '/tencent-phone-agent-cost',
    'xiaomi-phone-agent-summit': '/xiaomi-phone-agent-summit',
    'foneclaw-vs-likeclaw': '/foneclaw-vs-likeclaw',
    'foneclaw-vs-apple-intelligence': '/foneclaw-vs-apple-intelligence',
    'apple-intelligence-accessibility-foneclaw': '/apple-intelligence-accessibility-foneclaw',
    'foneclaw-vs-samsung-galaxy-ai': '/foneclaw-vs-samsung-galaxy-ai',
    'ai-phone-agent-harness': '/ai-phone-agent-harness',
    'mediatek-dimensity-phone-agent': '/mediatek-dimensity-phone-agent',
    'ios-27-siri-ai-agent': '/ios-27-siri-ai-agent',
    'ios-27-siri-gemini-integration': '/ios-27-siri-gemini-integration',
    'copilot-redesign-5-ai-trends-foneclaw': '/copilot-redesign-5-ai-trends-foneclaw',
    'ai-agent-spending-agentic-phone': '/ai-agent-spending-agentic-phone',
    'gemini-intelligence-pixel-9-excluded': '/gemini-intelligence-pixel-9-excluded',
    'samsung-galaxy-s26-ai-features-s25': '/samsung-galaxy-s26-ai-features-s25',
    'foneclaw-vs-openally': '/foneclaw-vs-openally',
    'foneclaw-vs-minimax': '/foneclaw-vs-minimax',
    'foneclaw-vs-all-in-one-ai-agent': '/foneclaw-vs-all-in-one-ai-agent',
    'foneclaw-vs-nebula-ai': '/foneclaw-vs-nebula-ai',
    'skyclaw-vs-foneclaw': '/skyclaw-vs-foneclaw',
    'foneclaw-vs-adobe-firefly': '/foneclaw-vs-adobe-firefly',
    'cloud-vs-local-ai-agent-2026': '/cloud-vs-local-ai-agent-2026',
    'microsoft-ai-super-app-vs-local-agent': '/microsoft-ai-super-app-vs-local-agent',
    'ai-agent-from-lab-to-pocket': '/ai-agent-from-lab-to-pocket',
    'hy-memory-vs-local-agent-memory': '/hy-memory-vs-local-agent-memory',
    'openclaw-security-risks-phone-agent-safer': '/openclaw-security-risks-phone-agent-safer',
    'gemini-spark-vs-foneclaw': '/gemini-spark-vs-foneclaw',
    'wwdc-2026-ai-do-over-phone-agent': '/wwdc-2026-ai-do-over-phone-agent',
    'personal-context-ai-agent-phone': '/personal-context-ai-agent-phone',
    'mcp-invisible-voice-control-phone-agent': '/mcp-invisible-voice-control-phone-agent',
    'apple-local-ai-validates-phone-agent': '/apple-local-ai-validates-phone-agent',
    'workbuddy-vs-foneclaw': '/workbuddy-vs-foneclaw',
    'microsoft-build-2026-ai-agents': '/microsoft-build-2026-ai-agents',
    'nvidia-ai-pc-vs-phone-ai-agent': '/nvidia-ai-pc-vs-phone-ai-agent',
    'apple-ai-glasses-vs-phone-agent': '/apple-ai-glasses-vs-phone-agent',
    'meta-ray-bans-ai-vs-foneclaw': '/meta-ray-bans-ai-vs-foneclaw',
    'ai-agents-rewriting-brand-discovery': '/ai-agents-rewriting-brand-discovery',
    'local-ai-agent-trust-vs-cloud': '/local-ai-agent-trust-vs-cloud',
    'enterprise-ai-agent-security-local': '/enterprise-ai-agent-security-local',
    'ai-agent-token-cost-local-saving': '/ai-agent-token-cost-local-saving',
    'app-intents-apps-machine-callable-ai-agents': '/app-intents-apps-machine-callable-ai-agents',
    'apple-intelligence-pro-subscription-what-to-expect': '/apple-intelligence-pro-subscription-what-to-expect',
    'microsoft-scout-openclaw-ai-agent': '/microsoft-scout-openclaw-ai-agent',
    'os-agent-three-layer-foundation-2026': '/os-agent-three-layer-foundation-2026',
    'ai-chip-custom-race-2026': '/ai-chip-custom-race-2026',
    'self-improving-ai-agents-phone': '/self-improving-ai-agents-phone',
    'eval-driven-phone-agent-measurement': '/eval-driven-phone-agent-measurement',
    'closed-loop-ai-phone-agent-human-in-loop': '/closed-loop-ai-phone-agent-human-in-loop',
    'on-device-llm-optimization-2026': '/on-device-llm-optimization-2026',
    'os-agent-vs-app-traffic-2026': '/os-agent-vs-app-traffic-2026',
    'openai-no-app-phone-voice-hack-night': '/openai-no-app-phone-voice-hack-night',
    'ai-agent-replaces-app-store-developers': '/ai-agent-replaces-app-store-developers',
    'voice-first-phone-2026-landscape': '/voice-first-phone-2026-landscape',
    'xiaomi-miclaw-user-review': '/xiaomi-miclaw-user-review',
    '1000-tps-llms-phone-agent-era': '/1000-tps-llms-phone-agent-era',
    'jd-tencent-ai-agent-shopping-phone-agent': '/jd-tencent-ai-agent-shopping-phone-agent',
    'wechat-ai-agent-commandable-super-app': '/wechat-ai-agent-commandable-super-app',
    'claude-code-multi-agent-system': '/claude-code-multi-agent-system',
}

# ── Article keyword index (load if available) ───────────────────────
try:
    from article_keywords_data import ARTICLE_KEYWORDS
except Exception:
    ARTICLE_KEYWORDS = {}

# ── Publish dates ───────────────────────────────────────────────────
try:
    from article_publish_dates import get_publish_date
except Exception:
    def get_publish_date(slug):
        return datetime.date.today().isoformat()

# ── Target articles: homepage (12) + resources page (12+ extras) ────
TARGET_SLUGS = [
    # First Taiwan rollout: same 12 featured articles as Simplified Chinese launch
    'tasker-alternative-voice-automation',
    'xiaomi-ai-ecosystem-2026',
    'voice-control-visually-impaired',
    'gemini-intelligence-supported-devices',
    'comp_vs_miclaw',
    'wwdc-2026-ai-do-over-phone-agent',
    'agentic-ai-phone-explained',
    'gemini-vs-foneclaw',
    'android-vs-ios-26-5-voice-control',
    'voice-control-whatsapp',
    'gemini-intelligence-vs-siri',
    'foneclaw-vs-apple-intelligence',
]

# ── Chinese translations for article titles and descriptions ────────
# Keys are article slugs, values are (tw_title, tw_description)
TW_TRANSLATIONS = {'tasker-alternative-voice-automation': ('Tasker 替代方案：Android 語音自動化', '不用 root，也能做 Android 語音自動化'),
 'xiaomi-ai-ecosystem-2026': ('小米 HyperOS AI 能力 2026', '小米 HyperOS AI 生態與 MiMo 模型'),
 'voice-control-visually-impaired': ('視障使用者手機語音控制指南', '為視障使用者整理的手機語音控制完整指南'),
 'gemini-intelligence-supported-devices': ('Gemini Intelligence 支援裝置整理 2026', '哪些手機可以用 Gemini Intelligence？一篇看懂支援範圍'),
 'comp_vs_miclaw': ('小米 MiClaw vs FoneClaw 比較', '小米 MiClaw 和 FoneClaw，適合哪一類使用者？'),
 'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026 Siri AI 和 Apple Intelligence', 'Apple 想把 Siri 帶向真正的手機龍蝦'),
 'agentic-ai-phone-explained': ('龍蝦式 AI 手機：MiClaw、Gemini、Siri AI', '手機 AI Agent 到底能做什麼？這篇一次說清楚'),
 'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw', 'Gemini 偏理解，FoneClaw 偏執行：差別在哪？'),
 'android-vs-ios-26-5-voice-control': ('Android vs iOS：語音控制比較 2026', 'Android 和 iOS 的語音控制，誰比較適合實用場景？'),
 'voice-control-whatsapp': ('WhatsApp 語音控制：免手動指南 2026', '用語音發 WhatsApp 訊息、打電話、管理聊天'),
 'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI：2026 比較', 'Gemini 和 Siri AI 的路線差異，一般使用者該怎麼看？'),
 'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'Apple 做系統 AI，FoneClaw 做 Android 執行能力')}

# ── Traditional Chinese (Taiwan) UI labels ───────────────────────────────────────────────
UI_LABELS = {'breadcrumb_home': '首頁',
 'breadcrumb_resources': '資源',
 'key_takeaways': '📋 重點整理',
 'contents': '📑 目錄',
 'faq_title': '常見問題',
 'read_suffix': '閱讀',
 'related_articles': '相關文章',
 'ready_cta': '準備好試試 FoneClaw？',
 'ready_copy': '下載最新 Android 安裝包，體驗 Android 9+ 上的 120+ 項手機操作。',
 'say_cta': '說一聲，就搞定。',
 'say_copy': '試用 FoneClaw，體驗權限清楚、執行前會確認的 Android 手機操作。'}

# Localized rewritten article bodies. Keep this as source-of-truth so
# regenerated Chinese articles do not fall back to English body text.
try:
    from tw_article_rewrites import TW_ARTICLE_REWRITES
except Exception:
    TW_ARTICLE_REWRITES = {}

FEATURED_TW_SLUGS = {
    'tasker-alternative-voice-automation',
    'xiaomi-ai-ecosystem-2026',
    'voice-control-visually-impaired',
    'gemini-intelligence-supported-devices',
    'comp_vs_miclaw',
    'wwdc-2026-ai-do-over-phone-agent',
    'agentic-ai-phone-explained',
    'gemini-vs-foneclaw',
    'android-vs-ios-26-5-voice-control',
    'voice-control-whatsapp',
    'gemini-intelligence-vs-siri',
    'foneclaw-vs-apple-intelligence',
}

CAT_ZH = {
    'Setup': '設定',
    'Tutorial': '教程',
    'Advanced': '进阶',
    'Guide': '指南',
    'Safety': '安全',
    'Smart Home': '智能家居',
    'Commuting': '通勤',
    'Accessibility': '無障礙',
    'Lifestyle': '生活方式',
    'Productivity': '效率',
    'Fitness': '健身',
    'Comparison': '比較',
    'Roundup': '盘点',
    'Industry': '產業',
    'Industry & Trends': '產業',
    'Industry and Trends': '產業',
    'Apps': 'App',
    'Social Media': '社交App',
    'Comparisons': '比較',
}

TW_INTERNAL_LINKS = {
    'tasker-alternative-voice-automation': [
        ('语音控制', 'android-vs-ios-26-5-voice-control'),
        ('WhatsApp', 'voice-control-whatsapp'),
        ('FoneClaw', 'gemini-vs-foneclaw'),
    ],
    'xiaomi-ai-ecosystem-2026': [
        ('MiClaw', 'comp_vs_miclaw'),
        ('手机端龙虾', 'agentic-ai-phone-explained'),
        ('Gemini Intelligence', 'gemini-intelligence-supported-devices'),
    ],
    'voice-control-visually-impaired': [
        ('语音控制', 'android-vs-ios-26-5-voice-control'),
        ('WhatsApp', 'voice-control-whatsapp'),
        ('FoneClaw', 'tasker-alternative-voice-automation'),
    ],
    'gemini-intelligence-supported-devices': [
        ('Gemini Intelligence', 'gemini-vs-foneclaw'),
        ('Siri', 'gemini-intelligence-vs-siri'),
        ('Android', 'android-vs-ios-26-5-voice-control'),
    ],
    'comp_vs_miclaw': [
        ('MiClaw', 'xiaomi-ai-ecosystem-2026'),
        ('手机龙虾', 'agentic-ai-phone-explained'),
        ('FoneClaw', 'gemini-vs-foneclaw'),
    ],
    'wwdc-2026-ai-do-over-phone-agent': [
        ('Apple Intelligence', 'foneclaw-vs-apple-intelligence'),
        ('Siri', 'gemini-intelligence-vs-siri'),
        ('Agentic AI', 'agentic-ai-phone-explained'),
    ],
    'agentic-ai-phone-explained': [
        ('MiClaw', 'comp_vs_miclaw'),
        ('Gemini', 'gemini-vs-foneclaw'),
        ('Siri', 'gemini-intelligence-vs-siri'),
    ],
    'gemini-vs-foneclaw': [
        ('Gemini Intelligence', 'gemini-intelligence-supported-devices'),
        ('Android', 'android-vs-ios-26-5-voice-control'),
        ('Apple Intelligence', 'foneclaw-vs-apple-intelligence'),
    ],
    'android-vs-ios-26-5-voice-control': [
        ('FoneClaw', 'tasker-alternative-voice-automation'),
        ('WhatsApp', 'voice-control-whatsapp'),
        ('Apple Intelligence', 'foneclaw-vs-apple-intelligence'),
        ('Gemini Intelligence', 'gemini-vs-foneclaw'),
    ],
    'voice-control-whatsapp': [
        ('FoneClaw', 'tasker-alternative-voice-automation'),
        ('免提', 'voice-control-visually-impaired'),
        ('语音控制', 'android-vs-ios-26-5-voice-control'),
    ],
    'gemini-intelligence-vs-siri': [
        ('Gemini Intelligence', 'gemini-intelligence-supported-devices'),
        ('Siri', 'wwdc-2026-ai-do-over-phone-agent'),
        ('Apple Intelligence', 'foneclaw-vs-apple-intelligence'),
    ],
    'foneclaw-vs-apple-intelligence': [
        ('Apple Intelligence', 'wwdc-2026-ai-do-over-phone-agent'),
        ('Android', 'android-vs-ios-26-5-voice-control'),
        ('Gemini Intelligence', 'gemini-vs-foneclaw'),
    ],
}


def _apply_zh_internal_links(text, current_slug, used_targets):
    """Add curated internal links to existing zh featured articles only."""
    for anchor, target in TW_INTERNAL_LINKS.get(current_slug, []):
        if target == current_slug or target not in FEATURED_TW_SLUGS or target in used_targets:
            continue
        if f'/tw/{target}.html' in text or '<a ' in text:
            continue
        pattern = re.escape(anchor)
        repl = f'<a href="/tw/{target}.html">{anchor}</a>'
        new_text, n = re.subn(pattern, repl, text, count=1)
        if n:
            used_targets.add(target)
            return new_text
    return text


def _slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower().strip()).strip('-')


def _make_hreflang_tags(slug):
    """Generate hreflang tags for an article page."""
    en_url = f'https://www.foneclaw.ai/{slug}.html'
    zh_url = f'https://www.foneclaw.ai/zh/{slug}.html'
    tw_url = f'https://www.foneclaw.ai/tw/{slug}.html'
    return (
        f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
        f'<link rel="alternate" hreflang="zh" href="{zh_url}">\n'
        f'<link rel="alternate" hreflang="zh-TW" href="{tw_url}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{en_url}">'
    )


def build_article_zh(art_data, output_slug=None):
    """Build a Chinese article page from article data tuple.

    Args:
        art_data: Article tuple (slug, title, desc, cat, read_time, sections)
        output_slug: The URL slug for the output file (may differ from art_data[0])
    """
    art_id = art_data[0]
    en_title = art_data[1]
    en_desc = art_data[2]
    cat = art_data[3]
    read_time = art_data[4]
    sections = art_data[5]

    # output_slug is the URL slug used for the file and canonical path
    if output_slug is None:
        output_slug = art_id

    # Get Chinese translations — try output_slug first, then art_id
    tw_title, tw_desc = TW_TRANSLATIONS.get(output_slug, TW_TRANSLATIONS.get(art_id, (en_title, en_desc)))

    # Use localized rewritten body when available. This prevents rebuilds from
    # overwriting the Chinese site with English article bodies.
    rewrite_sections = TW_ARTICLE_REWRITES.get(output_slug) or TW_ARTICLE_REWRITES.get(art_id)
    if rewrite_sections:
        sections = rewrite_sections

    url = URL_MAP.get(art_id, '/' + art_id)
    canonical = '/tw/' + output_slug + '.html'
    og_image = f'https://www.foneclaw.ai/images/articles/{art_id}.jpg'
    hreflang = _make_hreflang_tags(output_slug)

    html = []

    # ── Head ──
    html.append(head(
        f'{tw_title} - FoneClaw',
        tw_desc,
        canonical,
        extra_css='<style>.art-body p{text-indent:2em}.art-body li p{text-indent:0}</style>',
        og_image=og_image,
        lang='tw',
        hreflang_tags=hreflang,
    ))

    # ── Nav ──
    html.append(nav(3, lang='tw'))

    # ── Reading progress bar ──
    html.append('<div class="reading-progress" id="readProgress"></div>')

    html.append('<main>')
    html.append('<div class="art-wrap">')

    # ── Breadcrumb ──
    html.append(
        f'<div class="breadcrumb">'
        f'<a href="/tw/">{UI_LABELS["breadcrumb_home"]}</a>'
        f'<span class="sep">›</span>'
        f'<a href="/tw/resources.html">{UI_LABELS["breadcrumb_resources"]}</a>'
        f'<span class="sep">›</span>'
        f'<span>{tw_title}</span>'
        f'</div>'
    )

    # ── Article header ──
    html.append('<header class="art-header">')
    zh_cat = CAT_ZH.get(cat, cat)
    html.append(f'<div class="cat">{zh_cat}</div>')
    html.append('<div class="meta-row">')
    html.append(f'<span>📅 {datetime.date.today().strftime("%Y年%m月%d日")}</span>')
    if read_time:
        tw_read_time = str(read_time).replace(' min', ' 分鐘')
        html.append(f'<span>⏱️ {tw_read_time}閱讀</span>')
    html.append(
        '<span><img src="/images/author-dean.jpg" alt="Dean" '
        'style="width:20px;height:20px;border-radius:50%;vertical-align:middle;'
        'margin-right:6px;object-fit:cover">'
        '<a href="/author/dean.html" style="color:#00d4ff;text-decoration:none">'
        'Dean</a></span>'
    )
    html.append('</div>')
    html.append(f'<h1>{tw_title}</h1>')
    html.append(f'<p class="art-desc">{tw_desc}</p>')
    html.append('</header>')

    # ── Hero image ──
    html.append(
        f'<img class="art-hero" src="/images/articles/{art_id}.jpg" '
        f'alt="{tw_title}" loading="lazy">'
    )

    # ── Article APK CTA ──
    html.append(
        f'<div data-foneclaw-apk-cta data-variant="article" '
        f'data-title="{UI_LABELS["ready_cta"]}" '
        f'data-copy="{UI_LABELS["ready_copy"]}"></div>'
    )

    # ── Summary box ──
    html.append('<div class="summary-box">')
    html.append(f'<div class="box-title">{UI_LABELS["key_takeaways"]}</div>')
    html.append('<ul>')
    for sub, body in sections:
        if 'frequently asked' not in sub.lower():
            html.append(f'<li>{sub}</li>')
    html.append('</ul>')
    html.append('</div>')

    # ── Split sections: content vs FAQ ──
    def _is_faq_section(title):
        t = title.lower()
        return 'frequently asked' in t or '常見問題' in title

    content_sections = [(s, b) for s, b in sections if not _is_faq_section(s)]
    faq_sections = [(s, b) for s, b in sections if _is_faq_section(s)]

    # ── Table of Contents ──
    html.append('<div class="toc">')
    html.append(f'<div class="box-title">{UI_LABELS["contents"]}</div>')
    html.append('<ol>')
    for toc_idx, (sub, _) in enumerate(content_sections):
        slug = _slugify(sub) or f'section-{toc_idx+1}'
        html.append(f'<li><a href="#{slug}">{sub}</a></li>')
    if faq_sections:
        html.append(f'<li><a href="#faq">{UI_LABELS["faq_title"]}</a></li>')
    html.append('</ol>')
    html.append('</div>')

    # ── Article body (English content preserved) ──
    html.append('<div class="art-body">')

    linked_keywords = set()
    linked_targets = set()
    used_internal_targets = set()
    current_slug = art_id

    for idx, (sub, body) in enumerate(content_sections):
        slug = _slugify(sub) or f'section-{idx+1}'
        html.append(
            f'<h2 id="{slug}">'
            f'<a class="anchor" href="#{slug}" aria-hidden="true" tabindex="-1"></a>'
            f'{sub}</h2>'
        )
        paragraphs = [p.strip() for p in body.split('\n') if p.strip()]
        list_items = [p for p in paragraphs if p.startswith('- ') or p.startswith('* ')]
        non_list = [p for p in paragraphs if not (p.startswith('- ') or p.startswith('* '))]
        for para in non_list:
            para = _apply_zh_internal_links(para, output_slug, used_internal_targets)
            html.append(f'<p>{para}</p>')
        if list_items:
            html.append('<ul>')
            for item in list_items:
                html.append(f'<li>{item.lstrip("- *").strip()}</li>')
            html.append('</ul>')

    html.append('</div>')

    # ── FAQ accordion ──
    if faq_sections:
        html.append('<div class="art-faq">')
        html.append(
            f'<h2 id="faq">'
            f'<a class="anchor" href="#faq" aria-hidden="true" tabindex="-1"></a>'
            f'{UI_LABELS["faq_title"]}</h2>'
        )
        for _, faq_body in faq_sections:
            for q, a in _parse_faq(faq_body):
                safe_q = q.replace("'", "\\'").replace('"', '\\"')
                html.append(
                    f'<div class="faq-item" onclick="this.classList.toggle(\'open\');'
                    f'if(this.classList.contains(\'open\')){{var s=window.location.pathname'
                    f'.replace(/^\\//,\'\').replace(/\\.html$/,\'\');'
                    f'trackFAQ(\'{safe_q}\',s)}}">'
                )
                html.append(f'<div class="faq-q">{q}</div>')
                html.append(f'<div class="faq-a"><div class="faq-a-inner">{a}</div></div>')
                html.append('</div>')
        html.append('</div>')

    # ── Bottom CTA ──
    html.append(
        f'<div data-foneclaw-apk-cta '
        f'data-title="{UI_LABELS["say_cta"]}" '
        f'data-copy="{UI_LABELS["say_copy"]}"></div>'
    )

    # ── Related articles ──
    _cat_group = {
        'Setup': 'howto', 'Tutorial': 'howto', 'Advanced': 'howto', 'Guide': 'howto',
        'Safety': 'usecase', 'Smart Home': 'howto', 'Commuting': 'usecase',
        'Accessibility': 'usecase', 'Lifestyle': 'usecase', 'Productivity': 'usecase',
        'Fitness': 'usecase', 'Comparison': 'comp', 'Roundup': 'comp', 'Industry': 'comp',
    }
    _my_group = _cat_group.get(cat, 'other')
    _same, _related = [], []
    for item2 in articles_data:
        _rid, _rtitle = item2[0], item2[1]
        _rcat = item2[3]
        # Chinese publish package only includes the 12 featured articles.
        # Do not generate related links to removed/non-published zh pages.
        if _rid == art_id or _rid not in FEATURED_TW_SLUGS:
            continue
        _rg = _cat_group.get(_rcat, 'other')
        if _rg == _my_group:
            _same.append((_rid, _rtitle, _rcat))
        elif (_my_group == 'howto' and _rg == 'usecase') or \
             (_my_group == 'usecase' and _rg == 'howto') or \
             (_my_group == 'comp' and _rg == 'comp'):
            _related.append((_rid, _rtitle, _rcat))
    _picks = (_same + _related)[:3]
    if len(_picks) < 3:
        for item3 in articles_data:
            _rid, _rtitle, _rcat = item3[0], item3[1], item3[3]
            if _rid != art_id and _rid in FEATURED_TW_SLUGS and (_rid, _rtitle, _rcat) not in _picks:
                _picks.append((_rid, _rtitle, _rcat))
                if len(_picks) >= 3:
                    break

    html.append('<div class="related-section">')
    html.append(f'<h3>{UI_LABELS["related_articles"]}</h3>')
    html.append('<div class="related-grid">')
    # Build a reverse map: internal slug → URL slug for related articles
    _internal_to_url = {}
    for _is, _up in URL_MAP.items():
        _internal_to_url[_is] = _up.strip('/')

    for _rid, _rtitle, _rcat in _picks[:3]:
        _rurl_slug = _internal_to_url.get(_rid, _rid)
        if _rid == 'comp_vs_miclaw':
            _rurl_slug = 'comp_vs_miclaw'
        _rtw_title = TW_TRANSLATIONS.get(_rurl_slug, TW_TRANSLATIONS.get(_rid, (_rtitle, '')))[0]
        _rzh_cat = CAT_ZH.get(_rcat, _rcat)
        html.append(
            f'<a href="/tw/{_rurl_slug}.html" class="related-card">'
            f'<div class="rc-cat">{_rzh_cat}</div>'
            f'<div class="rc-title">{_rtw_title}</div>'
            f'</a>'
        )
    html.append('</div></div>')

    html.append('</div>')  # .art-wrap

    # ── JSON-LD Schemas ──
    _sch = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": tw_title,
        "description": tw_desc,
        "url": f"https://www.foneclaw.ai/tw/{output_slug}.html",
        "image": f"https://www.foneclaw.ai/images/articles/{art_id}.jpg",
        "author": {
            "@type": "Person",
            "name": "Dean",
            "url": "https://www.foneclaw.ai/author/dean.html",
        },
        "publisher": {
            "@type": "Organization",
            "name": "FoneClaw",
            "logo": {
                "@type": "ImageObject",
                "url": "https://www.foneclaw.ai/favicon.png",
            },
        },
        "datePublished": get_publish_date(art_id),
        "dateModified": datetime.date.today().isoformat(),
        "wordCount": sum(len(b.split()) for _, b in sections),
        "inLanguage": "zh",
    }
    html.append(
        '<script type="application/ld+json">'
        + json.dumps(_sch, ensure_ascii=False)
        + '</script>'
    )

    aq = []
    for _, fb in faq_sections:
        aq.extend(_parse_faq(fb))
    if aq:
        fs = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in aq
            ],
        }
        html.append(
            '<script type="application/ld+json">'
            + json.dumps(fs, ensure_ascii=False)
            + '</script>'
        )

    bc = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "首頁", "item": "https://www.foneclaw.ai/tw/"},
            {"@type": "ListItem", "position": 2, "name": "資源", "item": "https://www.foneclaw.ai/tw/resources.html"},
            {"@type": "ListItem", "position": 3, "name": tw_title, "item": f"https://www.foneclaw.ai/tw/{output_slug}.html"},
        ],
    }
    html.append(
        '<script type="application/ld+json">'
        + json.dumps(bc, ensure_ascii=False)
        + '</script>'
    )

    # ── Reading progress JS ──
    html.append('''<script>
window.addEventListener("scroll",function(){
  var e=document.getElementById("readProgress");
  if(!e)return;
  var h=document.documentElement.scrollHeight-window.innerHeight;
  var pct=h>0?Math.min(100,window.scrollY/h*100):0;
  e.style.width=pct+"%";
  var slug=window.location.pathname.replace(/^\\//,'').replace(/\\.html$/,'');
  if(pct>=25&&!window._s25){window._s25=1;trackScroll(25,slug);}
  if(pct>=50&&!window._s50){window._s50=1;trackScroll(50,slug);}
  if(pct>=75&&!window._s75){window._s75=1;trackScroll(75,slug);}
  if(pct>=100&&!window._s100){window._s100=1;trackScroll(100,slug);}
});
</script>''')

    # ── Outbound link tracking ──
    html.append('''<script>
document.addEventListener("click",function(e){
  var a=e.target.closest("a");
  if(!a)return;
  var href=a.getAttribute("href");
  if(href&&(href.startsWith("http://")||href.startsWith("https://"))&&!href.includes("foneclaw.ai")){
    var slug=window.location.pathname.replace(/^\\//,'').replace(/\\.html$/,'');
    trackOutbound(href,slug);
  }
});
</script>''')

    # ── Footer & social share ──
    html.append(footer(lang='tw'))
    html.append(social_share(lang='tw'))
    html.append(js())
    html.append('</body></html>')

    return '\n'.join(html)


def _parse_faq(body):
    """Parse FAQ text into list of (question, answer) tuples."""
    faqs = []
    q, a_lines = None, []
    for line in body.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('Q:') or (line.startswith('**Q') and '?' in line):
            if q and a_lines:
                faqs.append((q, ' '.join(a_lines)))
            q = line.lstrip('Q:').strip().strip('*').strip().rstrip('?').strip() + '?'
            a_lines = []
        elif line.startswith('A:') or line.startswith('**A'):
            a_lines.append(line.lstrip('A:').strip().strip('*').strip())
        elif q and a_lines:
            a_lines.append(line)
    if q and a_lines:
        faqs.append((q, ' '.join(a_lines)))
    return faqs


# ── Build article lookup by slug and by URL ─────────────────────────
articles_by_slug = {}
for item in articles_data:
    slug = item[0]
    articles_by_slug[slug] = item

# Build reverse lookup: URL path → internal slug
# Some articles have internal slugs (e.g. 'uc_visual_impaired') that map to
# different URL paths (e.g. '/voice-control-visually-impaired'). We need to
# find articles by their URL slug as well.
url_to_slug = {}
for internal_slug, url_path in URL_MAP.items():
    url_slug = url_path.strip('/')
    url_to_slug[url_slug] = internal_slug

# ── Generate Chinese article pages ─────────────────────────────────
os.makedirs(os.path.join(base, 'tw'), exist_ok=True)

generated = 0
missing = []

for slug in TARGET_SLUGS:
    # Try direct slug lookup first, then URL-based reverse lookup
    if slug in articles_by_slug:
        art_data = articles_by_slug[slug]
    elif slug in url_to_slug and url_to_slug[slug] in articles_by_slug:
        art_data = articles_by_slug[url_to_slug[slug]]
    else:
        missing.append(slug)
        continue
    html = build_article_zh(art_data, output_slug=slug)

    out_path = os.path.join(base, 'tw', f'{slug}.html')

    # Only write if content changed
    need_write = True
    if os.path.exists(out_path):
        with open(out_path, 'r', encoding='utf-8') as f:
            if f.read() == html:
                need_write = False

    if need_write:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        generated += 1
        print(f"  ✓ tw/{slug}.html ({len(html)//1024}KB)")
    else:
        print(f"  · tw/{slug}.html (unchanged)")

print(f"\nDone: {generated} Chinese article pages generated, "
      f"{len(TARGET_SLUGS) - generated - len(missing)} unchanged")
if missing:
    print(f"⚠ Missing articles (not in build data): {', '.join(missing)}")
