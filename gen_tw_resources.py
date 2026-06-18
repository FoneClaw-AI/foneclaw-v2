#!/usr/bin/env python3
"""Generate the Traditional Chinese (Taiwan) resources page from clean source data.

Avoid manual patching of tw/resources.html: repeated text replacements can pollute
article cards with duplicate <p> descriptions.
"""

from _components import full_page
from _homepage import _build_article_cards
from _i18n import generate_hreflang_tags

BASE = 'https://www.foneclaw.ai'

FEATURED_ARTICLES = [
    ('tasker-alternative-voice-automation', 'Tasker Alternative: Android Voice Automation', 'No-code voice automation for Android without root access.', 'Setup', '6 min'),
    ('xiaomi-ai-ecosystem-2026', 'Xiaomi HyperOS AI Capabilities 2026', 'MiMo model, HyperOS integration, and the Xiaomi app ecosystem.', 'Industry', '9 min'),
    ('voice-control-visually-impaired', 'Voice Activated Phone for Blind Users', '100% voice control for accessibility — Voice Access, TalkBack, and more.', 'Use Cases', '9 min'),
    ('gemini-intelligence-supported-devices', 'Gemini Intelligence Supported Devices List 2026', 'Which phones support Gemini Intelligence and what you need.', 'Industry', '10 min'),
    ('comp_vs_miclaw', 'Xiaomi MiClaw vs FoneClaw Phone Agent', 'Closed beta vs open Android — MiClaw, MiMo, and HyperOS lock-in.', 'Comparison', '7 min'),
    ('wwdc-2026-ai-do-over-phone-agent', 'WWDC 2026 Siri AI and Apple Intelligence', 'What Apple announced and what it means for phone agents.', 'Industry', '7 min'),
    ('agentic-ai-phone-explained', 'Agentic AI Phone: MiClaw, Gemini, Siri AI', 'What agentic AI means for your phone in 2026.', 'Industry', '8 min'),
    ('gemini-vs-foneclaw', 'Gemini Intelligence vs FoneClaw', 'Can Gemini Intelligence control Android apps like FoneClaw?', 'Comparison', '6 min'),
    ('android-vs-ios-26-5-voice-control', 'Android vs iOS: Voice Control Compared 2026', 'Voice assistant integration across platforms — who wins?', 'Comparison', '6 min'),
    ('voice-control-whatsapp', 'WhatsApp Voice Control: Hands-Free Guide 2026', 'Send messages, make calls, and manage chats with voice.', 'Apps', '7 min'),
    ('gemini-intelligence-vs-siri', 'Gemini Intelligence vs Siri AI: 2026 Comparison', 'WWDC 2026, Gemini-powered Siri, and what it means for Android.', 'Comparison', '20 min'),
    ('foneclaw-vs-apple-intelligence', 'FoneClaw vs Apple Intelligence', 'Siri AI vs Android agent — App Intents vs cross-app control.', 'Comparison', '12 min'),
]


def generate():
    article_cards = _build_article_cards(FEATURED_ARTICLES, lang='tw')
    extra_css = '''<style>
:root{--bg:#070914;--bg2:#0b1020;--panel:#101624;--line:rgba(255,255,255,.09);--line2:rgba(0,212,255,.18);--text:#f7f8fb;--muted:#9aa4b2;--cyan:#00d4ff}
.resources-hero{padding:86px 20px 60px;text-align:center;background:linear-gradient(135deg,#080c18 0%,#0b1a3a 50%,#080c18 100%)}
.resources-hero h1{font-size:clamp(32px,5vw,46px);font-weight:750;margin-bottom:12px;color:#f0f4f8;letter-spacing:-.02em}
.resources-hero p{color:#a5afbd;font-size:17px;line-height:1.75;max-width:660px;margin:0 auto}
.resources-section{padding:64px 0 80px}
.resources-title{text-align:center;margin-bottom:34px}
.resources-title h2{font-size:28px;font-weight:720;margin-bottom:8px;color:#f0f4f8}
.resources-title p{color:#8b949e;font-size:15px;margin:0}
.articles-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.article-card{background:var(--panel);border:1px solid var(--line);border-radius:16px;overflow:hidden;text-decoration:none;display:flex;flex-direction:column;transition:.25s;min-height:100%}
.article-card:hover{border-color:var(--line2);transform:translateY(-3px);box-shadow:0 10px 28px rgba(0,0,0,.18)}
.article-card-img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;background:#0d1117}
.article-card-body{padding:18px 18px 14px;display:flex;flex-direction:column;gap:8px;flex:1}
.article-card-tag{align-self:flex-start;background:rgba(0,212,255,.1);color:var(--cyan);padding:3px 10px;border-radius:8px;font-size:11px;font-weight:700;margin-bottom:2px}
.article-card-body h4{font-size:16px;font-weight:650;color:#f0f4f8;line-height:1.42;margin:0}
.article-card-body p{font-size:13px;color:#9aa4b2;line-height:1.65;margin:0;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.article-card-meta{display:flex;justify-content:space-between;align-items:center;padding:0 18px 18px;margin-top:auto}
.article-card-meta span{font-size:12px;color:var(--muted)}
.article-card-meta .read-link{color:var(--cyan);font-weight:600;font-size:13px}
@media(max-width:980px){.articles-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.resources-hero{padding-top:64px}.articles-grid{grid-template-columns:1fr}.article-card-body h4{font-size:15px}}
</style>'''
    body = f'''
<section class="resources-hero">
  <h1>資源中心</h1>
  <p>這裡整理了 FoneClaw 繁體中文指南、產品比較和 Android 語音控制深度分析。</p>
</section>
<section class="resources-section">
  <div class="wrap">
    <div class="resources-title">
      <h2>精選文章</h2>
      <p>從使用指南、產品比較到產業觀察，幫你更快理解 FoneClaw 和手機龍蝦生態。</p>
    </div>
    <div class="articles-grid">
      {article_cards}
    </div>
  </div>
</section>'''
    return full_page(
        'FoneClaw 資源中心 - Android 語音控制指南與深度分析',
        'FoneClaw 繁體中文資源中心：Android 語音控制指南、產品比較和手機龍蝦深度分析。',
        '/resources.html',
        3,
        body,
        extra_css=extra_css,
        og_image=f'{BASE}/images/og-index.jpg',
        lang='tw',
        hreflang_tags=generate_hreflang_tags('/resources.html', 'tw'),
    )


if __name__ == '__main__':
    from pathlib import Path
    out = Path('tw/resources.html')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(generate(), encoding='utf-8')
    print(f'wrote {out}')
