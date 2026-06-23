import datetime
try:
    from article_publish_dates import get_publish_date
except:
    def get_publish_date(slug): return datetime.date.today().isoformat()

# Helper: slugify heading text for anchor IDs
import re as _re, json as _json
from _social_share import social_share
def _slugify(text):
    return _re.sub(r'[^a-z0-9]+', '-', text.lower().strip()).strip('-')

# Helper: auto-bold key terms in paragraph text
_KEY_TERMS = [
    'FoneClaw', 'AI agent', 'voice control', 'voice commands', 'hands-free',
    'multi-step', 'cross-app', 'Android', 'Telegram', 'WhatsApp',
    'Google Maps', 'Spotify', 'DoorDash', 'iMessage', 'Amazon',
    'Accessibility Service', 'driving mode', 'Elderly Mode',
    'wake word', 'Barge-in', 'smart home', 'voice-first',
]
def _bold_terms(text):
    # First, protect link URLs from being bolded
    import re as _re2
    links = []
    def _save_link(m):
        links.append(m.group(0))
        return f'__LINK_{len(links)-1}__'
    
    # Save all <a href="...">...</a> tags
    protected = _re2.sub(r'<a\s+href="[^"]*"[^>]*>.*?</a>', _save_link, text)
    
    # Bold terms in non-link text
    for term in _KEY_TERMS:
        pattern = _re.compile(r'(?<![<\w/])(' + _re.escape(term) + r')(?![>\w])', _re.IGNORECASE)
        protected = pattern.sub(r'<strong>\1</strong>', protected)
    
    # Restore links
    for i, link in enumerate(links):
        protected = protected.replace(f'__LINK_{i}__', link)
    
    return protected

# Helper: auto-link keywords to related articles
def _auto_link_keywords(text, current_slug, keyword_index, linked_keywords, linked_targets=None):
    """Auto-link keywords in text to related articles."""
    import re as _re3
    
    # Initialize shared linked_targets if not provided
    if linked_targets is None:
        linked_targets = set()
    
    # Protect existing links and headings
    links = []
    def _save(m):
        links.append(m.group(0))
        return f'__PROTECT_{len(links)-1}__'
    
    protected = _re3.sub(r'<a\s[^>]*>.*?</a>', _save, text)
    protected = _re3.sub(r'<h[1-6][^>]*>.*?</h[1-6]>', _save, protected)
    
    # Protect markdown-style links [text](url.html) from being double-linked
    protected = _re3.sub(r'\[([^\]]+)\]\([^)]+\)', _save, protected)
    
    # Find and link keywords
    for target_slug, keywords in keyword_index.items():
        if target_slug == current_slug:
            continue
        
        # Skip if this target article is already linked
        target_url = f'/{target_slug}.html'
        if target_url in linked_targets:
            continue
        
        for keyword in keywords:
            if keyword.lower() in [k.lower() for k in linked_keywords]:
                continue
            
            # Case-insensitive replacement, only first occurrence
            pattern = _re3.compile(r'(?<![<\w/])(' + _re3.escape(keyword) + r')(?![>\w])', _re3.IGNORECASE)
            match = pattern.search(protected)
            if match:
                linked_text = match.group(1)
                replacement = f'<a href="{target_url}">{linked_text}</a>'
                protected = protected[:match.start()] + replacement + protected[match.end():]
                linked_keywords.add(keyword)
                linked_targets.add(target_url)
                break  # Only one keyword per target article
    
    # Restore protected content
    for i, link in enumerate(links):
        protected = protected.replace(f'__PROTECT_{i}__', link)
    
    return protected

# Helper: parse FAQ text into list of (question, answer) tuples
def _parse_faq(body):
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

count = 0
for _item in articles_data:
    if len(_item) >= 7:
        art_id, title, desc, cat, read_time, sections, share_text = _item[:7]
    else:
        art_id, title, desc, cat, read_time, sections = _item
        share_text = ''
    url = URL_MAP[art_id]
    html = []
    html.append(head(f'{title} - FoneClaw', desc, url + '.html', og_image=f'https://www.foneclaw.ai/images/articles/{art_id}.jpg'))
    html.append(nav(3))

    # Reading progress bar
    html.append('<div class="reading-progress" id="readProgress"></div>')

    html.append('<main>')
    html.append('<div class="art-wrap">')

    # Breadcrumb
    html.append('<div class="breadcrumb"><a href="/">Home</a><span class="sep">\u203a</span><a href="/resources.html">Resources</a><span class="sep">\u203a</span><span>' + title + '</span></div>')

    # Article header
    html.append('<header class="art-header">')
    html.append('<div class="cat">' + cat + '</div>')
    html.append('<div class="meta-row">')
    html.append('<span>\U0001f4c5 ' + datetime.date.today().strftime('%B %d, %Y') + '</span>')
    if read_time:
        html.append('<span>\u23f1\ufe0f ' + read_time + ' read</span>')
    html.append('<span><img src="/images/author-dean.jpg" alt="Dean" style="width:20px;height:20px;border-radius:50%;vertical-align:middle;margin-right:6px;object-fit:cover"><a href="/author/dean.html" style="color:#00d4ff;text-decoration:none">Dean</a></span>')
    html.append('</div>')
    html.append('<h1>' + title + '</h1>')
    html.append('<p class="art-desc">' + desc + '</p>')
    html.append('</header>')

    # Hero image
    html.append('<img class="art-hero" src="/images/articles/' + art_id + '.jpg" alt="' + title + '" loading="lazy">')

    # Article APK CTA
    html.append('<div data-foneclaw-apk-cta data-variant="article" data-title="Ready to try FoneClaw?" data-copy="Download the latest Android build for 120+ supported actions on Android 9+."></div>')

    # Summary box
    html.append('<div class="summary-box">')
    html.append('<div class="box-title">\U0001f4cb Key Takeaways</div>')
    html.append('<ul>')
    for sub, body in sections:
        if 'frequently asked' not in sub.lower():
            html.append('<li>' + sub + '</li>')
    html.append('</ul>')
    html.append('</div>')

    # Split sections: content vs FAQ
    content_sections = [(s, b) for s, b in sections if 'frequently asked' not in s.lower()]
    faq_sections = [(s, b) for s, b in sections if 'frequently asked' in s.lower()]

    # Table of Contents
    html.append('<div class="toc">')
    html.append('<div class="box-title">\U0001f4d1 Contents</div>')
    html.append('<ol>')
    for sub, _ in content_sections:
        slug = _slugify(sub)
        html.append('<li><a href="#' + slug + '">' + sub + '</a></li>')
    if faq_sections:
        html.append('<li><a href="#faq">Frequently Asked Questions</a></li>')
    html.append('</ol>')
    html.append('</div>')

    # Article body
    html.append('<div class="art-body">')

    # Track linked keywords to avoid duplicates
    linked_keywords = set()
    # Track linked targets to avoid linking same article twice
    linked_targets = set()
    # Get URL slug for keyword matching
    current_slug = URL_MAP.get(art_id, art_id).strip('/').replace('.html', '')

    for idx, (sub, body) in enumerate(content_sections):
        slug = _slugify(sub)
        html.append('<h2 id="' + slug + '"><a class="anchor" href="#' + slug + '" aria-label="Link to ' + sub.replace('\"','') + '"></a>' + sub + '</h2>')
        paragraphs = [p.strip() for p in body.split('\n') if p.strip()]
        list_items = [p for p in paragraphs if p.startswith('- ') or p.startswith('* ')]
        non_list = [p for p in paragraphs if not (p.startswith('- ') or p.startswith('* '))]
        for para_idx, para in enumerate(non_list):
            # Auto-link keywords to related articles
            para = _auto_link_keywords(para, current_slug, ARTICLE_KEYWORDS, linked_keywords, linked_targets)
            html.append('<p>' + _bold_terms(para) + '</p>')
        if list_items:
            html.append('<ul>')
            for item in list_items:
                item_text = item.lstrip('- *').strip()
                item_text = _auto_link_keywords(item_text, current_slug, ARTICLE_KEYWORDS, linked_keywords, linked_targets)
                html.append('<li>' + _bold_terms(item_text) + '</li>')
            html.append('</ul>')

    html.append('</div>')

    # FAQ accordion
    if faq_sections:
        html.append('<div class="art-faq">')
        html.append('<h2 id="faq"><a class="anchor" href="#faq" aria-label="Link to FAQ"></a>Frequently Asked Questions</h2>')
        for _, faq_body in faq_sections:
            for q, a in _parse_faq(faq_body):
                safe_q = q.replace("'", "\\'").replace('"', '\\"')
                html.append(f'<div class="faq-item" onclick="this.classList.toggle(\'open\');if(this.classList.contains(\'open\')){{var s=window.location.pathname.replace(/^\\//,\'\').replace(/\\.html$/,\'\');trackFAQ(\'{safe_q}\',s)}}">')
                html.append('<div class="faq-q">' + q + '</div>')
                html.append('<div class="faq-a"><div class="faq-a-inner">' + _bold_terms(a) + '</div></div>')
                html.append('</div>')
        html.append('</div>')

    # Bottom CTA
    html.append('<div data-foneclaw-apk-cta data-title="Say it. Done." data-copy="Try FoneClaw for supported Android phone actions with clear permissions and confirmation."></div>')

    # Related articles (smart matching by category)
    _cat_group = {'Setup':'howto','Tutorial':'howto','Advanced':'howto','Guide':'howto','Safety':'usecase','Smart Home':'howto',
                  'Commuting':'usecase','Accessibility':'usecase','Lifestyle':'usecase','Productivity':'usecase','Fitness':'usecase',
                  'Comparison':'comp','Roundup':'comp','Industry':'comp'}
    _my_group = _cat_group.get(cat, 'other')
    _same, _related = [], []
    for _item2 in articles_data:
        _rid, _rtitle = _item2[0], _item2[1]
        _rcat = _item2[3]
        if _rid == art_id: continue
        _rg = _cat_group.get(_rcat, 'other')
        if _rg == _my_group: _same.append((_rid, _rtitle, _rcat))
        elif (_my_group == 'howto' and _rg == 'usecase') or (_my_group == 'usecase' and _rg == 'howto') or (_my_group == 'comp' and _rg == 'comp'):
            _related.append((_rid, _rtitle, _rcat))
    _picks = (_same + _related)[:3]
    if len(_picks) < 3:
        for _item3 in articles_data:
            _rid, _rtitle, _rcat = _item3[0], _item3[1], _item3[3]
            if _rid != art_id and (_rid, _rtitle, _rcat) not in _picks:
                _picks.append((_rid, _rtitle, _rcat))
                if len(_picks) >= 3: break
    html.append('<div class="related-section">')
    html.append('<h3>Related Articles</h3>')
    html.append('<div class="related-grid">')
    for _rid, _rtitle, _rcat in _picks[:3]:
        html.append('<a href="' + URL_MAP[_rid] + '.html" class="related-card"><div class="rc-cat">' + _rcat + '</div><div class="rc-title">' + _rtitle + '</div></a>')
    html.append('</div></div>')

    html.append('</div>')

    # JSON-LD Schemas
    _sch = {"@context":"https://schema.org","@type":"TechArticle","headline":title,"description":desc,
        "url":"https://www.foneclaw.ai"+url+".html","image":"https://www.foneclaw.ai/images/articles/"+art_id+".jpg",
        "author":{"@type":"Person","name":"Dean","url":"https://www.foneclaw.ai/author/dean.html"},
        "publisher":{"@type":"Organization","name":"FoneClaw","logo":{"@type":"ImageObject","url":"https://www.foneclaw.ai/favicon.png"}},
        "datePublished":get_publish_date(art_id),"dateModified":datetime.date.today().isoformat(),"wordCount":sum(len(b.split()) for _,b in sections)}
    html.append('<script type="application/ld+json">' + _json.dumps(_sch, ensure_ascii=False) + '</script>')

    aq = []
    for _, fb in faq_sections:
        aq.extend(_parse_faq(fb))
    if aq:
        fs = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in aq]}
        html.append('<script type="application/ld+json">' + _json.dumps(fs, ensure_ascii=False) + '</script>')

    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":"https://www.foneclaw.ai/"},
        {"@type":"ListItem","position":2,"name":"Resources","item":"https://www.foneclaw.ai/resources.html"},
        {"@type":"ListItem","position":3,"name":title,"item":"https://www.foneclaw.ai"+url+".html"}]}
    html.append('<script type="application/ld+json">' + _json.dumps(bc, ensure_ascii=False) + '</script>')

    # Reading progress JS
    PROGRESS_JS = '''<script>
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
</script>'''
    html.append(PROGRESS_JS)

    # Outbound link tracking
    OUTBOUND_JS = '''<script>
document.addEventListener("click",function(e){
  var a=e.target.closest("a");
  if(!a)return;
  var href=a.getAttribute("href");
  if(href&&(href.startsWith("http://")||href.startsWith("https://"))&&!href.includes("foneclaw.ai")){
    var slug=window.location.pathname.replace(/^\\//,'').replace(/\\.html$/,'');
    trackOutbound(href,slug);
  }
});
</script>'''
    html.append(OUTBOUND_JS)

    html.append(footer())
    html.append(social_share(share_text))
    html.append(js(trans_json))
    html.append('</body></html>')

    fn = url.strip('/') + '.html'
    new_html = '\n'.join(html)
    
    # 只在内容变化时写入文件
    need_write = True
    html_path = os.path.join(base, fn)
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            existing_html = f.read()
        if existing_html == new_html:
            need_write = False
    
    if need_write:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        count += 1

print(f"[4/4] {count} article pages generated (new template)")
