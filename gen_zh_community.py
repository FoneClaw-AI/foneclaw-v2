#!/usr/bin/env python3
"""Generate Simplified Chinese community page from source-backed i18n."""
from pathlib import Path
from _components import head, nav, footer, js
from _social_share import social_share
from _i18n import get_text, generate_hreflang_tags

BASE = 'https://www.foneclaw.ai'

COMMUNITY_LINKS = [
    ('Telegram', '产品更新与 beta 消息', '加入', 'https://t.me/foneclaw'),
    ('Discord', '即时交流与开发讨论', '加入', 'https://discord.gg/vQ65DUHucj'),
    ('X', '最新消息与产品动态', '关注', 'https://x.com/huangda_huang'),
    ('Facebook', '社区更新与讨论', '关注', 'https://www.facebook.com/foneclaw'),
    ('YouTube', '视频教程与产品展示', '订阅', 'http://www.youtube.com/@foneclaw'),
    ('Instagram', '图片、短片与幕后内容', '关注', 'https://www.instagram.com/foneclaw/'),
    ('Reddit', '用户讨论与反馈', '加入', 'https://www.reddit.com/user/foneclaw/'),
    ('Feedback', '功能建议与问题反馈', '发邮件', 'mailto:Feedback@foneclaw.ai'),
]

def generate():
    title = get_text('community', 'meta_title', 'zh')
    desc = get_text('community', 'meta_desc', 'zh')
    hero_title = get_text('community', 'hero_title', 'zh')
    hero_desc = get_text('community', 'hero_desc', 'zh')
    extra_css = '''<style>
.community-hero{position:relative;min-height:300px;display:flex;align-items:center;justify-content:center;text-align:center;background:linear-gradient(135deg,#080c18 0%,#0b1a3a 50%,#080c18 100%)}
.community-hero:before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(0,212,255,.08) 0%,transparent 70%)}
.community-hero-inner{position:relative;z-index:1;padding:60px 20px}.community-hero h1{font-size:clamp(28px,5vw,44px);font-weight:700;margin-bottom:10px;color:#f0f4f8}.community-hero p{color:#8b949e;font-size:17px;max-width:620px;margin:0 auto;line-height:1.7}
.community-section{padding:40px 0 60px}.community-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.cc{background:var(--panel,#101624);border:1px solid var(--line,rgba(255,255,255,.09));border-radius:16px;padding:22px;text-align:center}.ci{font-size:30px;margin-bottom:10px}.cc h2{font-size:18px;font-weight:700;margin-bottom:6px;color:#f0f4f8}.cc p{font-size:13px;color:#8b949e;line-height:1.55;min-height:40px}.bs{display:inline-block;margin-top:12px;color:#00d4ff;text-decoration:none;font-weight:700;font-size:14px}
@media(max-width:980px){.community-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:560px){.community-grid{grid-template-columns:1fr}}
</style>'''
    icons = ['💬','🎮','𝕏','f','▶','◎','🤖','✉️']
    cards = []
    for icon, (name, detail, button, href) in zip(icons, COMMUNITY_LINKS):
        cards.append(f'<div class="cc"><div class="ci">{icon}</div><h2>{name}</h2><p>{detail}</p><a class="bs" href="{href}" target="_blank" rel="noopener">{button}</a></div>')
    body = f'''<section class="community-hero"><div class="community-hero-inner"><h1>{hero_title}</h1><p>{hero_desc}</p></div></section>
<section class="community-section"><div class="wrap"><div class="community-grid">{''.join(cards)}</div></div></section>'''
    html=[]
    html.append(head(title, desc, '/zh/community.html', extra_css=extra_css, og_image=f'{BASE}/images/home_arch.jpg', lang='zh', hreflang_tags=generate_hreflang_tags('/community.html','zh')))
    html.append(nav(4, 'zh'))
    html.append('<main>')
    html.append(body)
    html.append('</main>')
    html.append(footer('zh'))
    html.append(social_share(lang='zh'))
    html.append(js())
    html.append('</body></html>')
    return '\n'.join(html)

if __name__ == '__main__':
    out=Path('zh/community.html')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(generate(), encoding='utf-8')
    print(f'wrote {out}')
