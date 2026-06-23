"""Features page generation - v1.0.0 comprehensive design with 16 feature categories."""
import os, re


def generate_features_page(full_page, base, lang='en'):
    """Generate the new features page using full_page()."""
    from _i18n import get_text, generate_hreflang_tags
    t = lambda key: get_text('features', key, lang)
    ts = lambda key: get_text('features_showcase', key, lang)
    ts2 = lambda key: get_text('features_sections', key, lang)

    # Pre-compute translated strings
    _eyebrow = t('meta_title').split(' - ')[0] if ' - ' in t('meta_title') else 'FoneClaw Features'
    _hero_title = t('hero_title')
    _hero_lead = t('hero_lead')
    _cta_dl = t('cta_download')
    _cta_cp = t('cta_copy')
    _cta_exp = t('cta_explore')
    _stat_categories = '功能分類' if lang == 'tw' else ('功能分类' if lang == 'zh' else 'Categories')
    _stat_actions = '支援的操作' if lang == 'tw' else ('支持的操作' if lang == 'zh' else 'Supported actions')
    _cat_t = ts('cat_title')
    _cat_d = ts('cat_desc')
    _cmd_t = ts('cmd_title')
    _cmd_d = ts('cmd_desc')
    _mid_t = ts('bottom_cta_title')
    _trust_t = ts('trust_title')
    _trust_d = ts('trust_desc')
    _faq_t = ts('faq_title')
    _bot_t = ts('bottom_cta_title')
    _bot_d = ts('bottom_cta_desc')
    # Showcase translations
    _ey1 = ts2('eyebrow_phone'); _s1t = ts2('show1_title'); _s1d = ts2('show1_desc')
    _s1b1 = ts2('show1_b1'); _s1b2 = ts2('show1_b2'); _s1b3 = ts2('show1_b3')
    _ey2 = ts2('eyebrow_messages'); _s2t = ts2('show2_title'); _s2d = ts2('show2_desc')
    _s2b1 = ts2('show2_b1'); _s2b2 = ts2('show2_b2'); _s2b3 = ts2('show2_b3')
    _ey3 = ts2('eyebrow_controls'); _s3t = ts2('show3_title'); _s3d = ts2('show3_desc')
    _s3b1 = ts2('show3_b1'); _s3b2 = ts2('show3_b2'); _s3b3 = ts2('show3_b3')
    _ey4 = ts2('eyebrow_productivity'); _s4t = ts2('show4_title'); _s4d = ts2('show4_desc')
    _s4b1 = ts2('show4_b1'); _s4b2 = ts2('show4_b2'); _s4b3 = ts2('show4_b3')
    _ey5 = ts2('eyebrow_connectivity'); _s5t = ts2('show5_title'); _s5d = ts2('show5_desc')
    _s5b1 = ts2('show5_b1'); _s5b2 = ts2('show5_b2'); _s5b3 = ts2('show5_b3')
    _ey6 = ts2('eyebrow_passive'); _s6t = ts2('show6_title'); _s6d = ts2('show6_desc')
    _s6b1 = ts2('show6_b1'); _s6b2 = ts2('show6_b2'); _s6b3 = ts2('show6_b3'); _s6b4 = ts2('show6_b4')
    # Trust translations
    _t1t = ts2('trust1_title'); _t1b1 = ts2('trust1_b1'); _t1b2 = ts2('trust1_b2'); _t1b3 = ts2('trust1_b3')
    _t2t = ts2('trust2_title'); _t2d = ts2('trust2_desc')
    _t3t = ts2('trust3_title'); _t3d = ts2('trust3_desc')
    # FAQ translations
    _fq1q = ts2('faq1_q'); _fq1a = ts2('faq1_a'); _fq2q = ts2('faq2_q'); _fq2a = ts2('faq2_a')
    _fq3q = ts2('faq3_q'); _fq3a = ts2('faq3_a'); _fq4q = ts2('faq4_q'); _fq4a = ts2('faq4_a')
    _fq5q = ts2('faq5_q'); _fq5a = ts2('faq5_a')
    if lang == 'tw':
        _faq_sub = '幫你了解 FoneClaw 目前能做什麼，以及哪些操作需要確認。'
        _cat_phone, _cat_phone_n = '手機狀態', '9 個指令'
        _cat_notif, _cat_notif_n = '通知', '6 個指令'
        _cat_sms, _cat_sms_n = '簡訊', '6 個指令'
        _cat_calls, _cat_calls_n = '通話', '3 個指令'
        _cat_settings, _cat_settings_n = '系統設定', '18 個指令'
        _cat_conn, _cat_conn_n = 'Wi-Fi 與藍牙', '12 個指令'
        _cat_photo, _cat_photo_n = '拍照與截圖', '8 個指令'
        _cat_screen, _cat_screen_n = '螢幕讀取', '2 個指令'
        _cat_email, _cat_email_n = '信箱', '10 個指令'
        _cat_calendar, _cat_calendar_n = '行事曆', '6 個指令'
        _cat_alarms, _cat_alarms_n = '鬧鐘', '2 個指令'
        _cat_notes, _cat_notes_n = '筆記', '9 個指令'
        _cat_maps, _cat_maps_n = '地圖與導航', '8 個指令'
        _cat_web, _cat_web_n = '網頁', '3 個指令'
        _cat_workflows, _cat_workflows_n = '工作流程', '3 個指令'
        _cat_app, _cat_app_n = 'App 互動', '快速指令'
    elif lang == 'zh':
        _faq_sub = '帮你了解 FoneClaw 现在能做什么、哪些操作需要确认。'
        _cat_phone, _cat_phone_n = '手机状态', '9 条指令'
        _cat_notif, _cat_notif_n = '通知', '6 条指令'
        _cat_sms, _cat_sms_n = '短信', '6 条指令'
        _cat_calls, _cat_calls_n = '通话', '3 条指令'
        _cat_settings, _cat_settings_n = '系统设置', '18 条指令'
        _cat_conn, _cat_conn_n = 'Wi-Fi 与蓝牙', '12 条指令'
        _cat_photo, _cat_photo_n = '拍照与截图', '8 条指令'
        _cat_screen, _cat_screen_n = '屏幕读取', '2 条指令'
        _cat_email, _cat_email_n = '邮箱', '10 条指令'
        _cat_calendar, _cat_calendar_n = '日历', '6 条指令'
        _cat_alarms, _cat_alarms_n = '闹钟', '2 条指令'
        _cat_notes, _cat_notes_n = '笔记', '9 条指令'
        _cat_maps, _cat_maps_n = '地图与导航', '8 条指令'
        _cat_web, _cat_web_n = '网页', '3 条指令'
        _cat_workflows, _cat_workflows_n = '工作流', '3 条指令'
        _cat_app, _cat_app_n = '应用交互', '快捷指令'
    else:
        _faq_sub = 'Clear expectations help users understand what FoneClaw can do today.'
        _cat_phone, _cat_phone_n = 'Phone Status', '9 commands'
        _cat_notif, _cat_notif_n = 'Notifications', '6 commands'
        _cat_sms, _cat_sms_n = 'SMS', '6 commands'
        _cat_calls, _cat_calls_n = 'Calls', '3 commands'
        _cat_settings, _cat_settings_n = 'System Settings', '18 commands'
        _cat_conn, _cat_conn_n = 'Wi-Fi & Bluetooth', '12 commands'
        _cat_photo, _cat_photo_n = 'Photo & Screenshot', '8 commands'
        _cat_screen, _cat_screen_n = 'Screen Reading', '2 commands'
        _cat_email, _cat_email_n = 'Email', '10 commands'
        _cat_calendar, _cat_calendar_n = 'Calendar', '6 commands'
        _cat_alarms, _cat_alarms_n = 'Alarms', '2 commands'
        _cat_notes, _cat_notes_n = 'Notes', '9 commands'
        _cat_maps, _cat_maps_n = 'Maps & Navigation', '8 commands'
        _cat_web, _cat_web_n = 'Web', '3 commands'
        _cat_workflows, _cat_workflows_n = 'Workflows', '3 commands'
        _cat_app, _cat_app_n = 'App Interface', 'Quick commands'
    # Command translations
    _c1 = ts2('cmd1'); _c1d = ts2('cmd1_desc'); _c2 = ts2('cmd2'); _c2d = ts2('cmd2_desc')
    _c3 = ts2('cmd3'); _c3d = ts2('cmd3_desc'); _c4 = ts2('cmd4'); _c4d = ts2('cmd4_desc')
    _c5 = ts2('cmd5'); _c5d = ts2('cmd5_desc'); _c6 = ts2('cmd6'); _c6d = ts2('cmd6_desc')
    _c7 = ts2('cmd7'); _c7d = ts2('cmd7_desc'); _c8 = ts2('cmd8'); _c8d = ts2('cmd8_desc')

    extra_css = '''<style>
:root{--bg:#070914;--bg2:#0b1020;--panel:#101624;--panel2:#151c2d;--line:rgba(255,255,255,.09);--line2:rgba(0,212,255,.18);--text:#f7f8fb;--muted:#9aa4b2;--soft:#cbd5e1;--cyan:#00d4ff;--green:#3fb950;--violet:#7c7cff;--amber:#f7b955;--danger:#ff6b8a;--shadow:0 30px 80px rgba(0,0,0,.42);--radius:24px}
body:before{content:"";position:fixed;inset:0;pointer-events:none;background:radial-gradient(circle at 20% 0%,rgba(0,212,255,.16),transparent 32%),radial-gradient(circle at 84% 8%,rgba(124,124,255,.15),transparent 34%),radial-gradient(circle at 50% 100%,rgba(63,185,80,.08),transparent 36%);z-index:-2}
body:after{content:"";position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:56px 56px;mask-image:linear-gradient(to bottom,rgba(0,0,0,.72),transparent 72%);pointer-events:none;z-index:-1}
.hero{padding:110px 0 60px;position:relative}
.hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
@media(max-width:980px){.hero-grid{grid-template-columns:1fr}}
.eyebrow{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:2px;color:var(--cyan);margin-bottom:16px}
.hero h1{font-size:clamp(40px,6vw,60px);font-weight:700;line-height:1.08;letter-spacing:-.035em;margin-bottom:20px}
.grad{background:linear-gradient(135deg,var(--cyan),var(--green));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.lead{font-size:18px;color:var(--soft);line-height:1.7;margin-bottom:28px;max-width:520px}
.sub{font-size:15px;color:var(--muted);line-height:1.65;margin-bottom:28px;max-width:500px}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:32px}
.bp{padding:14px 32px;background:linear-gradient(135deg,var(--cyan),var(--green));color:#080c18;border:none;border-radius:12px;font-size:16px;font-weight:700;cursor:pointer;text-decoration:none;font-family:'Space Grotesk',sans-serif;display:inline-block}
.bo{padding:14px 32px;background:0;color:var(--soft);border:1px solid var(--line2);border-radius:12px;font-size:16px;cursor:pointer;font-family:'Space Grotesk',sans-serif;display:inline-block;text-decoration:none}
.hero-metrics{display:flex;gap:32px;flex-wrap:wrap}
.metric{display:flex;flex-direction:column}
.metric strong{font-size:28px;font-weight:800;color:var(--text);font-family:'Space Grotesk',sans-serif}
.metric span{font-size:13px;color:var(--muted)}
/* Hero screenshots placeholder */
.hero-screenshots{display:flex;gap:20px;align-items:center}
.phone-frame{display:inline-block;padding:10px 8px;background:#1a1d24;border-radius:24px;border:2px solid #2a2d35;box-shadow:0 8px 32px rgba(0,0,0,.4);flex-shrink:0;height:680px}.phone-frame img{display:block;border-radius:14px;width:100%;height:100%;object-fit:cover}.hero-phone{height:520px}.hero-gif{width:240px;height:520px}
@media(max-width:980px){.hero-gif{width:180px}}
@media(max-width:540px){.hero-screenshots{flex-direction:column;align-items:center}.hero-gif{width:220px}}
/* Section */
.section{padding:80px 0}
.section.alt{background:var(--bg2)}
.section-title{text-align:center;margin-bottom:48px}
.section-title h2{font-size:clamp(30px,4vw,42px);font-weight:700;margin-bottom:12px}
.section-title p{color:var(--muted);font-size:16px;max-width:600px;margin:0 auto;line-height:1.6}
/* Demo strip */
.demo-strip{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:980px){.demo-strip{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.demo-strip{grid-template-columns:1fr}}
.cmd{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:20px;transition:.2s}
.cmd:hover{border-color:var(--line2);transform:translateY(-2px)}
.num{font-size:11px;font-weight:800;color:var(--cyan);margin-bottom:8px;opacity:.6}
.cmd h3{font-size:15px;font-weight:600;margin-bottom:6px;color:var(--text)}
.cmd p{font-size:13px;color:var(--muted);line-height:1.5;margin:0}
/* Bento grid */
.bento{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:980px){.bento{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.bento{grid-template-columns:1fr}}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:24px;overflow:hidden;position:relative;display:flex;flex-direction:column}
.tile h3{font-size:17px;font-weight:700;margin-bottom:8px;color:var(--text)}
.tile p{font-size:13px;color:var(--muted);line-height:1.6;margin-bottom:14px;flex:1}
.tile .badge{display:inline-block;padding:3px 10px;border-radius:8px;font-size:11px;font-weight:700;background:rgba(0,212,255,.1);color:var(--cyan);margin-bottom:10px}
.tile .badge.coming{background:rgba(247,185,85,.12);color:var(--amber)}
.tile.large{grid-column:span 2}
@media(max-width:480px){.tile.large{grid-column:auto}}
.tile.wide{grid-column:span 2}
@media(max-width:480px){.tile.wide{grid-column:auto}}
/* Mock cards */
.mock-card{margin-top:auto;border-radius:18px;border:1px solid var(--line);background:radial-gradient(circle at 20% 20%,rgba(0,212,255,.1),transparent 38%),linear-gradient(180deg,rgba(255,255,255,.04),rgba(255,255,255,.02));padding:16px;min-height:160px;position:relative;overflow:hidden}
.tile.large .mock-card{min-height:200px}
.mock-title{font-size:11px;color:#c9f7ff;font-weight:700;margin-bottom:10px}
.mock-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.mock-stat{border:1px solid var(--line);background:rgba(255,255,255,.035);border-radius:12px;padding:10px}
.mock-stat b{display:block;color:#fff;font-size:18px;font-family:'Space Grotesk',sans-serif}
.mock-stat span{font-size:10px;color:var(--muted)}
.mock-line{height:8px;border-radius:999px;background:rgba(255,255,255,.06);margin:8px 0;overflow:hidden}
.mock-line:before{content:"";display:block;height:100%;width:var(--w,62%);border-radius:999px;background:linear-gradient(90deg,var(--cyan),var(--green))}
.mock-list{display:grid;gap:8px}
.mock-item{display:flex;gap:8px;align-items:center;border:1px solid var(--line);background:rgba(255,255,255,.035);border-radius:12px;padding:10px;color:var(--soft);font-size:12px}
.mock-icon{width:28px;height:28px;border-radius:8px;display:grid;place-items:center;background:linear-gradient(135deg,rgba(0,212,255,.2),rgba(124,124,255,.14));flex-shrink:0;font-size:14px}
.mock-scan{height:140px;border-radius:14px;border:1px solid rgba(0,212,255,.2);background:linear-gradient(135deg,rgba(0,212,255,.05),rgba(124,124,255,.06));position:relative;overflow:hidden}
.mock-scan:before{content:"";position:absolute;left:0;right:0;top:50%;height:2px;background:var(--cyan);box-shadow:0 0 20px var(--cyan)}
.mock-node{position:absolute;border:1px solid rgba(0,212,255,.4);background:rgba(0,212,255,.06);border-radius:6px}
.mock-node.a{left:20px;top:24px;width:100px;height:28px}
.mock-node.b{right:24px;top:64px;width:80px;height:44px}
.mock-node.c{left:36px;bottom:24px;width:60px;height:36px}
.mock-route{height:100px;border-radius:14px;border:1px solid var(--line);background:linear-gradient(135deg,rgba(63,185,80,.06),rgba(0,212,255,.06));position:relative;overflow:hidden}
.mock-route:before{content:"";position:absolute;left:20px;top:50%;width:calc(100% - 40px);height:2px;background:linear-gradient(90deg,var(--green),var(--cyan));border-radius:999px}
.mock-route:after{content:"";position:absolute;left:18px;top:calc(50% - 4px);width:8px;height:8px;border-radius:50%;background:var(--green)}
/* Showcase (zig-zag) */
.feature-flow{display:flex;flex-direction:column;gap:48px}
.showcase{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
@media(max-width:768px){.showcase{grid-template-columns:1fr;gap:24px}}
.showcase:nth-child(even) .show-text{order:2}
@media(max-width:768px){.showcase:nth-child(even) .show-text{order:0}}
.show-text h3{font-size:24px;font-weight:700;margin-bottom:12px;color:var(--text)}
.show-text p{font-size:15px;color:var(--muted);line-height:1.65;margin-bottom:16px}
.check-list{list-style:none;padding:0;margin:0}
.check-list li{padding:6px 0;font-size:14px;color:var(--soft);padding-left:20px;position:relative}
.check-list li:before{content:"";position:absolute;left:0;top:12px;width:8px;height:8px;border-radius:50%;background:var(--green)}
.visual{background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:24px;min-height:300px;display:flex;align-items:center;justify-content:center}
.scene-shot{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;width:280px;aspect-ratio:9/16;border:2px dashed rgba(0,212,255,.25);border-radius:16px;transition:border-color .3s;overflow:hidden;flex-shrink:0;margin:0 auto}
.scene-shot:hover{border-color:var(--cyan)}
.scene-icon{font-size:36px;opacity:.5}
.scene-label{font-size:13px;color:var(--muted);text-align:center}
/* Showcase image — supports both static and GIF */
.showcase-img{width:100%;height:auto;border-radius:16px;display:block}
@media(max-width:768px){.scene-shot{width:240px}}
/* Category overview grid */
.cat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
@media(max-width:980px){.cat-grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:680px){.cat-grid{grid-template-columns:repeat(2,1fr)}}
.cat-item{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px;text-align:center;transition:.2s}
.cat-item:hover{border-color:var(--line2);transform:translateY(-2px)}
.cat-item .emoji{font-size:28px;margin-bottom:8px;display:block}
.cat-item h4{font-size:13px;font-weight:700;color:var(--text);margin-bottom:4px}
.cat-item .count{font-size:11px;color:var(--muted)}
/* Category overview grid */
.cat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
@media(max-width:980px){.cat-grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:680px){.cat-grid{grid-template-columns:repeat(2,1fr)}}
.trust-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
@media(max-width:768px){.trust-grid{grid-template-columns:1fr}}
.trust{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:28px 24px;border-left:3px solid var(--cyan)}
.trust h3{font-size:17px;font-weight:700;margin-bottom:14px;color:var(--text)}
.trust p,.trust li{font-size:14px;color:var(--muted);line-height:1.7}
.trust ul{padding-left:18px;margin:0;list-style:disc}
.trust li{margin-bottom:6px}
.trust li:last-child{margin-bottom:0}
/* FAQ */
.faq{max-width:760px;margin:0 auto}
.fq{background:var(--panel);border:1px solid var(--line);border-radius:12px;margin-bottom:10px;overflow:hidden}
.fq-q{padding:16px 20px;cursor:pointer;font-size:15px;font-weight:600;color:var(--text);display:flex;justify-content:space-between;align-items:center;user-select:none}
.fq-q::after{content:"";color:var(--cyan);font-size:18px;transition:transform .2s}
.fq.on .fq-q::after{transform:rotate(45deg)}
.fq-a{max-height:0;overflow:hidden;transition:max-height .3s;padding:0 20px}
.fq.on .fq-a{max-height:300px;padding:0 20px 16px}
.fq-a p{font-size:14px;color:var(--muted);line-height:1.6;margin:0}
/* CTA */
.cta{text-align:center;padding:80px 20px;background:var(--bg2);border-top:1px solid var(--line)}
.cta h2{font-size:clamp(24px,3vw,32px);margin-bottom:12px}
.cta p{color:var(--muted);max-width:500px;margin:0 auto 28px;line-height:1.6}
/* Mid-page CTA */
.mid-cta{padding:40px 0;text-align:center;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.mid-cta h3{font-size:20px;margin-bottom:8px}
.mid-cta p{color:var(--muted);font-size:14px;margin-bottom:20px}
</style>'''

    body = f'''
<header class="hero">
  <div class="wrap hero-grid">
    <div>
      <div class="eyebrow">{_eyebrow}</div>
      <h1><span class="grad">{_hero_title}</span></h1>
      <p class="lead">{_hero_lead}</p>
      <div class="btns"><div data-foneclaw-apk-cta data-title="{_cta_dl}" data-copy="{_cta_cp}"></div><a class="bo" href="#showcases">{_cta_exp}</a></div>
      <div class="hero-metrics"><div class="metric"><strong>16</strong><span>{_stat_categories}</span></div><div class="metric"><strong>120+</strong><span>{_stat_actions}</span></div></div>
    </div>
    <div class="hero-screenshots" aria-label="Product screenshots">
      <div class="phone-frame hero-phone"><img src="/images/features/gif-phone-health-poster.jpg" data-gif="/images/features/gif-phone-health.gif" alt="FoneClaw phone health report" class="hero-gif lazy-gif"></div>
      <div class="phone-frame hero-phone"><img src="/images/features/gif-daily-brief-poster.jpg" data-gif="/images/features/gif-daily-brief.gif" alt="FoneClaw daily brief" class="hero-gif lazy-gif"></div>
    </div>
  </div>
</header>

<section class="section alt">
  <div class="wrap">
    <div class="section-title"><h2>{_cat_t}</h2><p>{_cat_d}</p></div>
    <div class="cat-grid">
      <div class="cat-item"><span class="emoji">\U0001f4f1</span><h4>{_cat_phone}</h4><span class="count">{_cat_phone_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f514</span><h4>{_cat_notif}</h4><span class="count">{_cat_notif_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f4ac</span><h4>{_cat_sms}</h4><span class="count">{_cat_sms_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f4de</span><h4>{_cat_calls}</h4><span class="count">{_cat_calls_n}</span></div>
      <div class="cat-item"><span class="emoji">\u2699\ufe0f</span><h4>{_cat_settings}</h4><span class="count">{_cat_settings_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f4e1</span><h4>{_cat_conn}</h4><span class="count">{_cat_conn_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f4f8</span><h4>{_cat_photo}</h4><span class="count">{_cat_photo_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f5a5\ufe0f</span><h4>{_cat_screen}</h4><span class="count">{_cat_screen_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f4e7</span><h4>{_cat_email}</h4><span class="count">{_cat_email_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f4c5</span><h4>{_cat_calendar}</h4><span class="count">{_cat_calendar_n}</span></div>
      <div class="cat-item"><span class="emoji">\u23f0</span><h4>{_cat_alarms}</h4><span class="count">{_cat_alarms_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f4cb</span><h4>{_cat_notes}</h4><span class="count">{_cat_notes_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f5fa\ufe0f</span><h4>{_cat_maps}</h4><span class="count">{_cat_maps_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f310</span><h4>{_cat_web}</h4><span class="count">{_cat_web_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f504</span><h4>{_cat_workflows}</h4><span class="count">{_cat_workflows_n}</span></div>
      <div class="cat-item"><span class="emoji">\U0001f9e9</span><h4>{_cat_app}</h4><span class="count">{_cat_app_n}</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-title"><h2>{_cmd_t}</h2><p>{_cmd_d}</p></div>
    <div class="demo-strip">
      <div class="cmd"><div class="num">01</div><h3>"{_c1}"</h3><p>{_c1d}</p></div>
      <div class="cmd"><div class="num">02</div><h3>"{_c2}"</h3><p>{_c2d}</p></div>
      <div class="cmd"><div class="num">03</div><h3>"{_c3}"</h3><p>{_c3d}</p></div>
      <div class="cmd"><div class="num">04</div><h3>"{_c4}"</h3><p>{_c4d}</p></div>
      <div class="cmd"><div class="num">05</div><h3>"{_c5}"</h3><p>{_c5d}</p></div>
      <div class="cmd"><div class="num">06</div><h3>"{_c6}"</h3><p>{_c6d}</p></div>
      <div class="cmd"><div class="num">07</div><h3>"{_c7}"</h3><p>{_c7d}</p></div>
      <div class="cmd"><div class="num">08</div><h3>"{_c8}"</h3><p>{_c8d}</p></div>
    </div>
  </div>
</section>

<section class="mid-cta"><div class="wrap"><h3>{_mid_t}</h3><p>{_bot_d}</p><div data-foneclaw-apk-cta data-title="{_cta_dl}" data-copy="{_cta_cp}"></div></div></section>

<section class="section alt" id="showcases">
  <div class="wrap feature-flow">
    <div class="showcase">
      <div class="show-text"><div class="eyebrow">{_ey1}</div><h3>{_s1t}</h3><p>{_s1d}</p><ul class="check-list"><li>{_s1b1}</li><li>{_s1b2}</li><li>{_s1b3}</li></ul></div>
      <div class="visual"><div class="phone-frame"><img src="/images/features/gif-phone-health-poster.jpg" data-gif="/images/features/gif-phone-health.gif" alt="Phone Health" class="showcase-img lazy-gif"></div></div>
    </div>
    <div class="showcase">
      <div class="show-text"><div class="eyebrow">{_ey2}</div><h3>{_s2t}</h3><p>{_s2d}</p><ul class="check-list"><li>{_s2b1}</li><li>{_s2b2}</li><li>{_s2b3}</li></ul></div>
      <div class="visual"><div class="phone-frame"><img src="/images/features/gif-daily-brief-poster.jpg" data-gif="/images/features/gif-daily-brief.gif" alt="Daily Brief" class="showcase-img lazy-gif"></div></div>
    </div>
    <div class="showcase">
      <div class="show-text"><div class="eyebrow">{_ey3}</div><h3>{_s3t}</h3><p>{_s3d}</p><ul class="check-list"><li>{_s3b1}</li><li>{_s3b2}</li><li>{_s3b3}</li></ul></div>
      <div class="visual"><div class="phone-frame"><img src="/images/features/gif-controls-poster.jpg" data-gif="/images/features/gif-controls.gif" alt="Controls" class="showcase-img lazy-gif"></div></div>
    </div>
    <div class="showcase">
      <div class="show-text"><div class="eyebrow">{_ey4}</div><h3>{_s4t}</h3><p>{_s4d}</p><ul class="check-list"><li>{_s4b1}</li><li>{_s4b2}</li><li>{_s4b3}</li></ul></div>
      <div class="visual"><div class="phone-frame"><img src="/images/features/gif-productivity-poster.jpg" data-gif="/images/features/gif-productivity.gif" alt="Productivity" class="showcase-img lazy-gif"></div></div>
    </div>
    <div class="showcase">
      <div class="show-text"><div class="eyebrow">{_ey5}</div><h3>{_s5t}</h3><p>{_s5d}</p><ul class="check-list"><li>{_s5b1}</li><li>{_s5b2}</li><li>{_s5b3}</li></ul></div>
      <div class="visual"><div class="phone-frame"><img src="/images/features/gif-connectivity-poster.jpg" data-gif="/images/features/gif-connectivity.gif" alt="Connectivity" class="showcase-img lazy-gif"></div></div>
    </div>
    <div class="showcase">
      <div class="show-text"><div class="eyebrow">{_ey6}</div><h3>{_s6t}</h3><p>{_s6d}</p><ul class="check-list"><li>{_s6b1}</li><li>{_s6b2}</li><li>{_s6b3}</li><li>{_s6b4}</li></ul></div>
      <div class="visual"><div class="phone-frame"><img src="/images/features/gif-passive-triggers-poster.jpg" data-gif="/images/features/gif-passive-triggers.gif" alt="Passive Triggers" class="showcase-img lazy-gif"></div></div>
    </div>
  </div>
</section>

<section class="mid-cta"><div class="wrap"><h3>{_bot_t}</h3><p>{_bot_d}</p><div data-foneclaw-apk-cta data-title="{_cta_dl}" data-copy="{_cta_cp}"></div></div></section>

<section class="section alt">
  <div class="wrap">
    <div class="section-title"><h2>{_trust_t}</h2><p>{_trust_d}</p></div>
    <div class="trust-grid">
      <div class="trust"><h3>{_t1t}</h3><ul><li>{_t1b1}</li><li>{_t1b2}</li><li>{_t1b3}</li></ul></div>
      <div class="trust"><h3>{_t2t}</h3><p>{_t2d}</p></div>
      <div class="trust"><h3>{_t3t}</h3><p>{_t3d}</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-title"><h2>{_faq_t}</h2><p>{_faq_sub}</p></div>
    <div class="faq">
      <div class="fq"><div class="fq-q" onclick="this.parentElement.classList.toggle(\'on\')">{_fq1q}</div><div class="fq-a"><p>{_fq1a}</p></div></div>
      <div class="fq"><div class="fq-q" onclick="this.parentElement.classList.toggle(\'on\')">{_fq2q}</div><div class="fq-a"><p>{_fq2a}</p></div></div>
      <div class="fq"><div class="fq-q" onclick="this.parentElement.classList.toggle(\'on\')">{_fq3q}</div><div class="fq-a"><p>{_fq3a}</p></div></div>
      <div class="fq"><div class="fq-q" onclick="this.parentElement.classList.toggle(\'on\')">{_fq4q}</div><div class="fq-a"><p>{_fq4a}</p></div></div>
      <div class="fq"><div class="fq-q" onclick="this.parentElement.classList.toggle('on')">{_fq5q}</div><div class="fq-a"><p>{_fq5a}</p></div></div>
    </div>
  </div>
</section>

<section class="cta"><div class="wrap"><h2>{_bot_t}</h2><p>{_bot_d}</p><div data-foneclaw-apk-cta data-title="{_cta_dl}" data-copy="{_cta_cp}"></div></div></section>
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

    hreflang = generate_hreflang_tags('/features.html', lang)

    return full_page(
        t('meta_title'),
        t('meta_desc'),
        '/features.html' if lang == 'en' else f'/{lang}/features.html',
        1,
        body,
        extra_css=extra_css,
        og_image='https://www.foneclaw.ai/images/og-features.jpg',
        lang=lang,
        hreflang_tags=hreflang
    )
