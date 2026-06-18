"""Resources page - uses full_page() for consistent styling"""
import os
from _i18n import generate_hreflang_tags

def generate_resources_page(full_page, base):
    """Generate resources page using full_page()"""
    
    hub_css = """<style>
.res-hero{background:linear-gradient(135deg,#080c18 0%,#0b1a3a 50%,#080c18 100%);padding:80px 20px 60px;text-align:center;position:relative;overflow:hidden}
.res-hero::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:url('/images/hub/resources-hero.jpg') center/cover;opacity:0.15}
.res-hero>*{position:relative;z-index:1}
.res-hero h1{font-size:clamp(32px,5vw,48px);font-weight:700;margin-bottom:12px;color:#f0f4f8}
.res-hero p{color:#8b949e;font-size:18px;max-width:500px;margin:0 auto 24px}
.res-stats{display:flex;justify-content:center;gap:48px;margin:32px 0}
.res-stat{text-align:center}.res-stat .num{font-size:2rem;font-weight:700;color:#00d4ff}.res-stat .label{font-size:0.85rem;color:#8b949e;text-transform:uppercase;letter-spacing:1px}
.res-cta{display:flex;gap:16px;justify-content:center;margin-top:24px}
.hub-grid{max-width:1100px;margin:60px auto;padding:0 20px;display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
.hub-card{background:#161b22;border:1px solid #21262d;border-radius:16px;overflow:hidden;transition:all 0.3s;display:block;text-decoration:none}.hub-card:hover{border-color:#00d4ff;transform:translateY(-4px);box-shadow:0 12px 40px rgba(0,212,255,0.15)}
.hub-card-img{height:200px;background-size:cover;background-position:center}.hub-card-body{padding:28px}
.hub-card-count{display:inline-block;background:#21262d;color:#8b949e;padding:4px 12px;border-radius:12px;font-size:0.8rem;font-weight:600;margin-bottom:12px}
.hub-card-title{font-size:1.4rem;font-weight:700;color:#f0f4f8;margin-bottom:8px}.hub-card-desc{color:#8b949e;font-size:0.95rem;margin-bottom:16px;line-height:1.6}
.hub-card-link{color:#00d4ff;font-weight:600;display:flex;align-items:center;gap:6px}
.featured{max-width:1100px;margin:60px auto;padding:0 20px}.featured h2{font-size:1.8rem;font-weight:700;margin-bottom:28px;color:#f0f4f8}
.featured-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.featured-card{background:#161b22;border:1px solid #21262d;border-radius:12px;padding:24px;transition:all 0.3s;display:block;text-decoration:none}.featured-card:hover{border-color:#00d4ff;transform:translateY(-2px)}
.featured-tag{display:inline-block;background:rgba(63,185,80,0.1);color:#3fb950;padding:3px 10px;border-radius:8px;font-size:0.75rem;font-weight:600;margin-bottom:10px}
.featured-title{font-size:1rem;font-weight:600;color:#f0f4f8;margin-bottom:8px;line-height:1.4}.featured-desc{color:#8b949e;font-size:0.85rem;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.cta-section{background:#161b22;border-top:1px solid #21262d;padding:80px 20px;text-align:center;margin-top:60px}.cta-section h2{font-size:2rem;margin-bottom:12px;color:#f0f4f8}.cta-section p{color:#8b949e;margin-bottom:28px;font-size:1.1rem}
@media(max-width:768px){.hub-grid{grid-template-columns:1fr}.featured-grid{grid-template-columns:1fr}.res-stats{flex-direction:column;gap:16px}.hub-card-img{height:160px}}
</style>"""
    
    res_body = """
<section class="res-hero">
  <h1>Resources</h1>
  <p>120+ guides, tutorials, and analyses for voice-controlled Android</p>
  <div class="res-stats">
    <div class="res-stat"><div class="num">120+</div><div class="label">Articles</div></div>
    <div class="res-stat"><div class="num">4</div><div class="label">Topics</div></div>
    <div class="res-stat"><div class="num">40+</div><div class="label">Hours</div></div>
  </div>
  <div class="res-cta">
    <a href="#topics" class="bp">Browse Topics</a>
    <a href="/download.html" class="bo">Get FoneClaw</a>
  </div>
</section>
<section class="hub-grid" id="topics">
  <a href="/voice-control/index.html" class="hub-card"><div class="hub-card-img" style="background:url('/images/hub/hub-card-voice-control.jpg') center/cover"></div><div class="hub-card-body"><span class="hub-card-count">36 guides</span><h3 class="hub-card-title">Voice Control</h3><p class="hub-card-desc">Control WhatsApp, YouTube, TikTok, and 30+ apps with your voice.</p><span class="hub-card-link">Explore Voice Control</span></div></a>
  <a href="/comparisons/index.html" class="hub-card"><div class="hub-card-img" style="background:url('/images/hub/hub-card-comparisons.jpg') center/cover"></div><div class="hub-card-body"><span class="hub-card-count">46 guides</span><h3 class="hub-card-title">Comparisons</h3><p class="hub-card-desc">Head-to-head analysis with Siri, Alexa, Google Assistant, and 20+ competitors.</p><span class="hub-card-link">Explore Comparisons</span></div></a>
  <a href="/ai-agent/index.html" class="hub-card"><div class="hub-card-img" style="background:url('/images/hub/hub-card-ai-agent.jpg') center/cover"></div><div class="hub-card-body"><span class="hub-card-count">27 guides</span><h3 class="hub-card-title">AI Agent</h3><p class="hub-card-desc">Deep dives into phone AI agent architecture and the future of mobile AI.</p><span class="hub-card-link">Explore AI Agent</span></div></a>
  <a href="/news/index.html" class="hub-card"><div class="hub-card-img" style="background:url('/images/hub/hub-card-news.jpg') center/cover"></div><div class="hub-card-body"><span class="hub-card-count">17 articles</span><h3 class="hub-card-title">Industry News</h3><p class="hub-card-desc">Latest announcements from Apple, Google, Xiaomi, and the AI ecosystem.</p><span class="hub-card-link">Explore News</span></div></a>
</section>
<section class="featured">
  <h2>Featured Articles</h2>
  <div class="featured-grid">
    <a href="/voice-control-android.html" class="featured-card"><span class="featured-tag">Most Popular</span><h3 class="featured-title">Voice Control Android: Complete Setup Guide</h3><p class="featured-desc">Everything you need to know about setting up voice control.</p></a>
    <a href="/foneclaw-vs-siri.html" class="featured-card"><span class="featured-tag">Top Comparison</span><h3 class="featured-title">FoneClaw vs Siri: Voice Assistant Comparison</h3><p class="featured-desc">Local AI agent vs Apple cloud-based assistant.</p></a>
    <a href="/agentic-ai-phone-explained.html" class="featured-card"><span class="featured-tag">AI Deep Dive</span><h3 class="featured-title">Agentic AI on Your Phone: What It Means</h3><p class="featured-desc">The complete explainer on how AI agents work.</p></a>
    <a href="/jd-tencent-ai-agent-shopping-phone-agent.html" class="featured-card"><span class="featured-tag">Shopping Agents</span><h3 class="featured-title">JD Tencent AI Agent: Shopping Agents Begin</h3><p class="featured-desc">Why shopping agents need phone execution, approval, and real app control.</p></a>
    <a href="/wechat-ai-agent-commandable-super-app.html" class="featured-card"><span class="featured-tag">WeChat AI</span><h3 class="featured-title">WeChat AI Agent: Commandable Super App</h3><p class="featured-desc">Where super app agents end and phone agents begin.</p></a>
    <a href="/claude-code-multi-agent-system.html" class="featured-card"><span class="featured-tag">Claude Code</span><h3 class="featured-title">Claude Code Multi-Agent System</h3><p class="featured-desc">What AI coding agents teach phone agents about delegation, verification, and safe execution.</p></a>
    <a href="/ai-phone-war-2026.html" class="featured-card"><span class="featured-tag">Hot News</span><h3 class="featured-title">AI Phone War 2026: The Battle Begins</h3><p class="featured-desc">OpenAI vs ByteDance vs Google.</p></a>
    <a href="/best-voice-control-apps-2026.html" class="featured-card"><span class="featured-tag">Ranking</span><h3 class="featured-title">Best Voice Control Apps 2026</h3><p class="featured-desc">Ranking of every major voice control solution.</p></a>
    <a href="/android-vs-ios-26-5-voice-control.html" class="featured-card"><span class="featured-tag">Platform Comparison</span><h3 class="featured-title">Android vs iOS: Voice Control Compared 2026</h3><p class="featured-desc">Which OS offers better voice assistant integration and hands-free automation.</p></a>
    <a href="/voice-control-whatsapp.html" class="featured-card"><span class="featured-tag">App Guide</span><h3 class="featured-title">WhatsApp Voice Control: Hands-Free Guide 2026</h3><p class="featured-desc">Send messages, make calls, and search chats with your voice.</p></a>
    <a href="/gemini-intelligence-supported-devices.html" class="featured-card"><span class="featured-tag">Gemini Devices</span><h3 class="featured-title">Gemini Intelligence Supported Devices List 2026</h3><p class="featured-desc">Check Pixel, Samsung, Xiaomi, OnePlus, and Android compatibility.</p></a>
  </div>
</section>
<section class="cta-section">
  <h2>Ready to Try FoneClaw?</h2>
  <p>Start controlling your Android phone with your voice today.</p>
  <a href="/download.html" class="bp">Download FoneClaw Free</a>
</section>"""
    
    # Use full_page() with CSS in <head>
    return full_page(
        "Resources - FoneClaw",
        "120+ guides, tutorials, and analyses for voice-controlled Android. Browse by topic: Voice Control, Comparisons, AI Agent, Industry News.",
        "/resources.html",
        3,  # Resources active
        res_body,
        extra_css=hub_css,  # CSS goes in <head>!
        og_image="https://www.foneclaw.ai/images/hub/resources-hero.jpg",
        lang='en',
        hreflang_tags=generate_hreflang_tags('/resources.html', 'en')
    )
