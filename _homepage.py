"""Homepage generation - FoneClaw pre-release redesign with new slogan and 120+ actions positioning."""


ZH_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('Tasker 替代方案：Android 语音自动化', '无需 root 的 Android 语音自动化方案'),
    'xiaomi-ai-ecosystem-2026': ('小米 HyperOS AI 能力 2026', '小米 HyperOS AI 生态和 MiMo 模型'),
    'voice-control-visually-impaired': ('视障用户语音控制手机指南', '视障用户的语音手机控制完全指南'),
    'gemini-intelligence-supported-devices': ('Gemini Intelligence 支持设备整理 2026', '哪些手机能用 Gemini Intelligence？一文看懂兼容范围'),
    'comp_vs_miclaw': ('小米 MiClaw vs FoneClaw 对比', '小米 MiClaw 和 FoneClaw，到底适合谁？'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026 Siri AI 和 Apple Intelligence', '苹果这次想把 Siri 带向真正的手机龙虾'),
    'agentic-ai-phone-explained': ('龙虾式 AI 手机：MiClaw、Gemini、Siri AI', '手机 AI Agent 到底能做什么？这篇讲清楚'),
    'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw', 'Gemini 偏理解，FoneClaw 偏执行：差别在哪？'),
    'android-vs-ios-26-5-voice-control': ('Android vs iOS：语音控制对比 2026', 'Android 和 iOS 的语音控制，到底谁更适合实用场景？'),
    'voice-control-whatsapp': ('WhatsApp 语音控制：免提指南 2026', '用语音发 WhatsApp 消息、打电话、管理聊天'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI：2026 对比', 'Gemini 和 Siri AI 的路线差异，普通用户该怎么看？'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', '苹果做系统 AI，FoneClaw 做 Android 执行能力'),
}

TW_TRANSLATIONS = {'tasker-alternative-voice-automation': ('Tasker 替代方案：Android 語音自動化', '不用 root，也能做 Android 語音自動化'),
 'xiaomi-ai-ecosystem-2026': ('小米 HyperOS AI 能力 2026', '小米 HyperOS AI 生態與 MiMo 模型'),
 'voice-control-visually-impaired': ('視障使用者手機語音控制指南', '為視障使用者整理的手機語音控制完整指南'),
 'gemini-intelligence-supported-devices': ('Gemini Intelligence 支援裝置整理 2026', '哪些手機可以用 Gemini Intelligence？一篇看懂支援範圍'),
 'comp_vs_miclaw': ('小米 MiClaw vs FoneClaw 比較', '小米 MiClaw 和 FoneClaw，適合哪一類使用者？'),
 'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026 Siri AI 和 Apple Intelligence', 'Apple 想把 Siri 帶向真正的手機龍蝦'),
 'agentic-ai-phone-explained': ('龍蝦式 AI 手機：MiClaw、Gemini、Siri AI', '手機 AI Agent 到底能做什麼？這篇一次說清楚'),
 'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw', 'Gemini 偏理解，FoneClaw 偏執行：差別在哪？'),
 'android-vs-ios-26-5-voice-control': ('Android vs iOS：語音控制比較 2026', 'Android 和 iOS 的語音控制，誰更適合實用場景？'),
 'voice-control-whatsapp': ('WhatsApp 語音控制：免手動指南 2026', '用語音發 WhatsApp 訊息、打電話、管理聊天'),
 'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI：2026 比較', 'Gemini 和 Siri AI 的路線差異，一般使用者該怎麼看？'),
 'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'Apple 做系統 AI，FoneClaw 做 Android 執行能力')}


def _build_article_cards(articles, lang='en'):
    """Build HTML for article cards with hub-style design."""
    # slug → (url, image) overrides for mismatched paths
    overrides = {
        'voice-control-visually-impaired': ('voice-control-visually-impaired', 'uc_visual_impaired'),
        'gemini-vs-foneclaw': ('gemini-vs-foneclaw', 'comp_vs_gemini'),
        'comp_vs_miclaw': ('miclaw-vs-foneclaw', 'comp_vs_miclaw'),
    }
    cards = []
    for slug, title, desc, cat, read_time in articles:
        if lang == 'tw' and slug in TW_TRANSLATIONS:
            title, desc = TW_TRANSLATIONS[slug]
        elif lang == 'zh' and slug in ZH_TRANSLATIONS:
            title, desc = ZH_TRANSLATIONS[slug]
        read_label = '閱讀' if lang == 'tw' else ('阅读' if lang == 'zh' else 'Read')
        prefix = '/tw' if lang == 'tw' else ('/zh' if lang == 'zh' else '')
        url_slug, img_slug = overrides.get(slug, (slug, slug))
        if lang in ('zh', 'tw') and slug == 'comp_vs_miclaw':
            url_slug = 'comp_vs_miclaw'
        if lang in ('zh', 'tw'):
            read_time = str(read_time).replace(' min', ' 分鐘' if lang == 'tw' else ' 分钟')
            zh_cat = {'Setup': '设置','Industry': '行业','Use Cases': '使用场景','Comparison': '对比','Apps': '应用','Guide': '指南','Safety': '安全','Accessibility': '无障碍'}
            tw_cat = {'Setup': '設定','Industry': '產業','Use Cases': '使用情境','Comparison': '比較','Apps': 'App','Guide': '指南','Safety': '安全','Accessibility': '無障礙'}
            cat = (tw_cat if lang == 'tw' else zh_cat).get(cat, cat)
        img_html = f'<img class="article-card-img" src="/images/articles/{img_slug}.jpg" alt="{title}" loading="lazy" onerror="this.style.display=\'none\'">'
        cards.append(
            f'<a href="{prefix}/{url_slug}.html" class="article-card">'
            f'{img_html}'
            f'<div class="article-card-body">'
            f'<span class="article-card-tag">{cat}</span>'
            f'<h4>{title}</h4>'
            f'<p>{desc[:120]}</p>'
            f'</div>'
            f'<div class="article-card-meta"><span>⏱ {read_time}</span><span class="read-link">{read_label} →</span></div>'
            f'</a>'
        )
    return '\n      '.join(cards)


def generate_homepage(full_page, base, imgs=None, lang='en'):
    """Generate the homepage using full_page()."""
    from _i18n import get_text, generate_hreflang_tags

    t = lambda key: get_text('homepage', key, lang)

    # Featured articles — from Google Sheet optimization tracking
    featured_articles = [
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
    article_cards_html = _build_article_cards(featured_articles, lang=lang)

    _free_label = '免費' if lang == 'tw' else ('免费' if lang == 'zh' else 'Free')

    extra_css = '''<style>
:root{--bg:#070914;--bg2:#0b1020;--panel:#101624;--panel2:#151c2d;--line:rgba(255,255,255,.09);--line2:rgba(0,212,255,.18);--text:#f7f8fb;--muted:#9aa4b2;--soft:#cbd5e1;--cyan:#00d4ff;--green:#3fb950;--violet:#7c7cff;--amber:#f7b955;--danger:#ff6b8a;--radius:24px}
body:before{content:"";position:fixed;inset:0;pointer-events:none;background:radial-gradient(circle at 20% 0%,rgba(0,212,255,.16),transparent 32%),radial-gradient(circle at 84% 8%,rgba(124,124,255,.15),transparent 34%),radial-gradient(circle at 50% 100%,rgba(63,185,80,.08),transparent 36%);z-index:-2}
body:after{content:"";position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:56px 56px;mask-image:linear-gradient(to bottom,rgba(0,0,0,.72),transparent 72%);pointer-events:none;z-index:-1}
/* Hero */
.hero{padding:120px 0 80px;text-align:center}
.hero h1{font-size:clamp(48px,8vw,72px);font-weight:800;line-height:1.05;letter-spacing:-.04em;margin-bottom:20px}
.hero .grad{background:linear-gradient(135deg,var(--cyan),var(--green));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero .lead{font-size:18px;color:var(--soft);line-height:1.7;max-width:580px;margin:0 auto 32px}
.hero .btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:48px}
.bp{padding:14px 32px;background:linear-gradient(135deg,var(--cyan),var(--green));color:#080c18;border:none;border-radius:12px;font-size:16px;font-weight:700;cursor:pointer;text-decoration:none;font-family:'Space Grotesk',sans-serif;display:inline-block;transition:.2s}
.bp:hover{box-shadow:0 4px 20px rgba(0,212,255,.3);transform:translateY(-1px)}
.bo{padding:14px 32px;background:0;color:var(--soft);border:1px solid var(--line2);border-radius:12px;font-size:16px;cursor:pointer;font-family:'Space Grotesk',sans-serif;display:inline-block;text-decoration:none;transition:.2s}
.bo:hover{border-color:var(--cyan);color:var(--text)}
.hero-screenshots{display:flex;gap:20px;justify-content:center;align-items:center}
.phone-frame{display:inline-block;padding:10px 8px;background:#1a1d24;border-radius:24px;border:2px solid #2a2d35;box-shadow:0 8px 32px rgba(0,0,0,.4);flex-shrink:0;height:420px}.phone-frame img{display:block;border-radius:14px;width:100%;height:100%;object-fit:cover}.hero-gif{width:auto;height:420px;max-width:240px}
@media(max-width:980px){.hero-gif{width:180px}}
@media(max-width:540px){.hero-screenshots{flex-direction:column;align-items:center}.hero-gif{width:220px}}
/* Scenarios */
.scenarios{padding:80px 0;background:var(--bg2)}
.section-title{text-align:center;margin-bottom:48px}
.section-title h2{font-size:clamp(28px,4vw,40px);font-weight:700;margin-bottom:10px}
.section-title p{color:var(--muted);font-size:16px;max-width:560px;margin:0 auto;line-height:1.6}
.scenario-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
@media(max-width:768px){.scenario-grid{grid-template-columns:1fr}}
.scenario{background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:28px 24px;text-align:center;transition:.25s}
.scenario:hover{border-color:var(--line2);transform:translateY(-3px)}
.scenario .emoji{font-size:36px;margin-bottom:14px;display:block}
.scenario h3{font-size:18px;font-weight:700;margin-bottom:8px;color:var(--text)}
.scenario p{font-size:14px;color:var(--muted);line-height:1.65}
/* Stats bar */
.stats{padding:60px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats-grid{display:flex;justify-content:center;gap:60px;flex-wrap:wrap}
.stat{text-align:center}
.stat strong{display:block;font-size:36px;font-weight:800;color:var(--text);font-family:'Space Grotesk',sans-serif}
.stat span{font-size:13px;color:var(--muted)}
/* Feature overview */
.features-overview{padding:80px 0;background:var(--bg2)}
.feat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:768px){.feat-grid{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.feat-grid{grid-template-columns:1fr}}
.feat{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:22px;transition:.25s}
.feat:hover{border-color:var(--line2);transform:translateY(-2px)}
.feat .emoji{font-size:24px;margin-bottom:10px;display:block}
.feat h4{font-size:15px;font-weight:700;margin-bottom:4px;color:var(--text)}
.feat p{font-size:13px;color:var(--muted);line-height:1.5}
.feat-link{display:inline-block;margin-top:24px;font-size:15px;color:var(--cyan);font-weight:600;text-decoration:none}
.feat-link:hover{text-decoration:underline}
/* Trust */
.trust{padding:80px 0}
.trust-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
@media(max-width:768px){.trust-grid{grid-template-columns:1fr}}
.trust-card{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:28px 24px;border-left:3px solid var(--cyan)}
.trust-card h3{font-size:17px;font-weight:700;margin-bottom:10px;color:var(--text)}
.trust-card p{font-size:14px;color:var(--muted);line-height:1.7}
/* FAQ */
.faq{max-width:720px;margin:0 auto}
.fq{background:var(--panel);border:1px solid var(--line);border-radius:12px;margin-bottom:8px;overflow:hidden;cursor:pointer}
.fq-q{padding:16px 20px;font-size:15px;font-weight:600;color:var(--text);display:flex;justify-content:space-between;align-items:center}
.fq-q::after{content:"+";color:var(--cyan);font-size:18px;transition:.2s}
.fq.on .fq-q::after{transform:rotate(45deg)}
.fq-a{max-height:0;overflow:hidden;transition:.3s;padding:0 20px;color:var(--muted);font-size:14px;line-height:1.7}
.fq.on .fq-a{max-height:300px;padding:0 20px 16px}
/* Bottom CTA */
.bottom-cta{padding:80px 0;text-align:center;background:var(--bg2);border-top:1px solid var(--line)}
.bottom-cta h2{font-size:clamp(24px,3.5vw,36px);margin-bottom:12px}
.bottom-cta p{color:var(--muted);max-width:480px;margin:0 auto 28px;line-height:1.6}
/* Featured articles */
.articles-section{padding:80px 0;background:var(--bg2)}
.articles-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
@media(max-width:980px){.articles-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:540px){.articles-grid{grid-template-columns:1fr}}
.article-card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;text-decoration:none;display:block;transition:.25s}
.article-card:hover{border-color:var(--line2);transform:translateY(-3px)}
.article-card-img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.article-card-body{padding:18px}
.article-card-tag{display:inline-block;background:rgba(0,212,255,.1);color:var(--cyan);padding:3px 10px;border-radius:8px;font-size:11px;font-weight:700;margin-bottom:8px}
.article-card h4{font-size:15px;font-weight:700;color:var(--text);margin-bottom:6px;line-height:1.35}
.article-card p{font-size:13px;color:var(--muted);line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.article-card-meta{display:flex;justify-content:space-between;align-items:center;padding:0 18px 14px}
.article-card-meta span{font-size:12px;color:var(--muted)}
.article-card-meta .read-link{color:var(--cyan);font-weight:600;font-size:13px}
/* Filter tabs */
.filter-tabs{display:flex;gap:10px;justify-content:center;margin-bottom:32px;flex-wrap:wrap}
.filter-tab{padding:8px 18px;background:var(--panel);border:1px solid var(--line);border-radius:20px;color:var(--muted);font-size:13px;font-weight:600;cursor:pointer;transition:.2s;text-decoration:none;font-family:'Space Grotesk',sans-serif}
.filter-tab:hover,.filter-tab.on{border-color:var(--cyan);color:var(--cyan);background:rgba(0,212,255,.06)}
</style>'''

    _features_href = '/tw/features.html' if lang == 'tw' else ('/zh/features.html' if lang == 'zh' else '/features.html')
    body = '''
<header class="hero">
  <div class="wrap">
    <h1><span class="grad">''' + t('hero_slogan') + '''</span></h1>
    <p class="lead">''' + t('hero_lead') + '''</p>
    <div data-foneclaw-apk-cta data-title="''' + t('cta_download') + '''" data-copy="''' + t('cta_copy') + '''"></div>
    <div style="text-align:center;margin-top:16px;margin-bottom:40px"><a class="bo" href="''' + _features_href + '''">''' + t('cta_see_features') + '''</a></div>
    <div class="hero-screenshots" aria-label="Product screenshots">
      <div class="phone-frame"><img src="/images/features/gif-phone-health-poster.jpg" data-gif="/images/features/gif-phone-health.gif" alt="FoneClaw phone health" class="hero-gif lazy-gif"></div>
      <div class="phone-frame"><img src="/images/features/gif-daily-brief-poster.jpg" data-gif="/images/features/gif-daily-brief.gif" alt="FoneClaw daily brief" class="hero-gif lazy-gif"></div>
      <div class="phone-frame"><img src="/images/features/gif-passive-triggers-poster.jpg" data-gif="/images/features/gif-passive-triggers.gif" alt="FoneClaw passive triggers" class="hero-gif lazy-gif"></div>
    </div>
  </div>
</header>

<section class="scenarios">
  <div class="wrap">
    <div class="section-title"><h2>''' + t('scenario_title') + '''</h2><p>''' + t('scenario_desc') + '''</p></div>
    <div class="scenario-grid">
      <div class="scenario"><span class="emoji">\U0001f4e2</span><h3>''' + t('scenario_1_title') + '''</h3><p>''' + t('scenario_1_desc') + '''</p></div>
      <div class="scenario"><span class="emoji">\U0001f4f1</span><h3>''' + t('scenario_2_title') + '''</h3><p>''' + t('scenario_2_desc') + '''</p></div>
      <div class="scenario"><span class="emoji">\U0001f4f8</span><h3>''' + t('scenario_3_title') + '''</h3><p>''' + t('scenario_3_desc') + '''</p></div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="wrap">
    <div class="stats-grid">
      <div class="stat"><strong>16</strong><span>''' + t('stat_categories') + '''</span></div>
      <div class="stat"><strong>120+</strong><span>''' + t('stat_actions') + '''</span></div>
      <div class="stat"><strong>''' + _free_label + '''</strong><span>''' + t('stat_free') + '''</span></div>
      <div class="stat"><strong>Android 9+</strong><span>''' + t('stat_android') + '''</span></div>
    </div>
  </div>
</section>



<section class="articles-section">
  <div class="wrap">
    <div class="section-title"><h2>''' + t('articles_title') + '''</h2><p>''' + t('articles_desc') + '''</p></div>
    <div class="articles-grid">
      {article_cards_html}
    </div>
  </div>
</section>

<section class="bottom-cta">
  <div class="wrap">
    <h2>''' + t('bottom_cta_title') + '''</h2>
    <p>''' + t('bottom_cta_desc') + '''</p>
    <div data-foneclaw-apk-cta data-title="''' + t('cta_download') + '''" data-copy="''' + t('cta_copy') + '''"></div>
  </div>
</section>
<script>
document.querySelectorAll('.lazy-gif').forEach(function(img){{
  var poster=img.src;
  var gif=img.getAttribute('data-gif');
  if(!gif)return;
  img.addEventListener('mouseenter',function(){{img.src=gif;}});
  img.addEventListener('mouseleave',function(){{img.src=poster;}});
}});
</script>
'''

    body = body.format(article_cards_html=article_cards_html)

    hreflang = generate_hreflang_tags('/', lang)

    return full_page(
        t('meta_title'),
        t('meta_desc'),
        '/' if lang == 'en' else f'/{lang}/',
        0,
        body,
        extra_css=extra_css,
        og_image='https://www.foneclaw.ai/images/og-index.jpg',
        lang=lang,
        hreflang_tags=hreflang)
