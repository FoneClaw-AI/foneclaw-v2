# Social media sharing component for FoneClaw website

def social_share(share_text='', lang='en'):
    """Social media sharing sidebar component - returns HTML + JS.
    
    Args:
        share_text: Optional custom share text (<=280 chars). 
                    If empty, falls back to page title + meta description.
        lang: Language code ('en' or 'zh'). Default 'en'.
    """
    # Escape share_text for JS injection
    safe_text = share_text.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n').replace('\r', '')
    
    # Build JS variable for custom share text
    js_var = "var __customShareText='" + safe_text + "';" if safe_text else "var __customShareText='';"
    
    # Localized button titles and toast text
    if lang == 'tw':
        labels = {
            'x': '分享到 X',
            'telegram': '分享到 Telegram',
            'linkedin': '分享到 LinkedIn',
            'facebook': '分享到 Facebook',
            'reddit': '分享到 Reddit',
            'copy': '複製連結',
            'toast': '連結已複製！',
        }
    elif lang == 'zh':
        labels = {
            'x': '分享到 X',
            'telegram': '分享到 Telegram',
            'linkedin': '分享到 LinkedIn',
            'facebook': '分享到 Facebook',
            'reddit': '分享到 Reddit',
            'copy': '复制链接',
            'toast': '链接已复制！',
        }
    else:
        labels = {
            'x': 'Share on X',
            'telegram': 'Share on Telegram',
            'linkedin': 'Share on LinkedIn',
            'facebook': 'Share on Facebook',
            'reddit': 'Share on Reddit',
            'copy': 'Copy link',
            'toast': 'Link copied!',
        }
    
    x_btn = '<button onclick="shareToX()" title="' + labels['x'] + '" style="width:40px;height:40px;border-radius:50%;background:#0d1117;border:1px solid #21262d;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;color:#8b949e"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></button>'

    html = '''
<div id="social-share" style="position:fixed;right:20px;top:120px;z-index:9999;display:flex;flex-direction:column;gap:8px">
''' + x_btn + '''
<button onclick="shareToTelegram()" title="' + labels['telegram'] + '" style="width:40px;height:40px;border-radius:50%;background:#0d1117;border:1px solid #21262d;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;color:#8b949e"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg></button>
<button onclick="shareToLinkedIn()" title="' + labels['linkedin'] + '" style="width:40px;height:40px;border-radius:50%;background:#0d1117;border:1px solid #21262d;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;color:#8b949e"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></button>
<button onclick="shareToFacebook()" title="' + labels['facebook'] + '" style="width:40px;height:40px;border-radius:50%;background:#0d1117;border:1px solid #21262d;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;color:#8b949e"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></button>
<button onclick="shareToReddit()" title="' + labels['reddit'] + '" style="width:40px;height:40px;border-radius:50%;background:#0d1117;border:1px solid #21262d;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;color:#8b949e"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0zm5.01 4.744c.688 0 1.25.561 1.25 1.249a1.25 1.25 0 0 1-2.498.056l-2.597-.547-.8 3.747c1.824.07 3.48.632 4.674 1.488.308-.309.73-.491 1.207-.491.968 0 1.754.786 1.754 1.754 0 .716-.435 1.333-1.01 1.614a3.111 3.111 0 0 1 .042.52c0 2.694-3.13 4.87-7.004 4.87-3.874 0-7.004-2.176-7.004-4.87 0-.183.015-.366.043-.534A1.748 1.748 0 0 1 4.028 12c0-.968.786-1.754 1.754-1.754.463 0 .898.196 1.207.49 1.207-.883 2.878-1.43 4.744-1.487l.885-4.182a.342.342 0 0 1 .14-.197.35.35 0 0 1 .238-.042l2.906.617a1.214 1.214 0 0 1 1.108-.701zM9.25 12C8.561 12 8 12.562 8 13.25c0 .687.561 1.248 1.25 1.248.687 0 1.248-.561 1.248-1.249 0-.688-.561-1.249-1.249-1.249zm5.5 0c-.687 0-1.248.561-1.248 1.25 0 .687.561 1.248 1.249 1.248.688 0 1.249-.561 1.249-1.249 0-.687-.562-1.249-1.25-1.249zm-5.466 3.99a.327.327 0 0 0-.231.094.33.33 0 0 0 0 .463c.842.842 2.484.913 2.961.913.477 0 2.105-.056 2.961-.913a.361.361 0 0 0 .029-.463.33.33 0 0 0-.464 0c-.547.533-1.684.73-2.512.73-.828 0-1.979-.196-2.512-.73a.326.326 0 0 0-.232-.095z"/></svg></button>
<button onclick="copyLink()" title="' + labels['copy'] + '" style="width:40px;height:40px;border-radius:50%;background:#0d1117;border:1px solid #21262d;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;color:#8b949e"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg></button>
</div>
<div id="copy-toast" style="display:none;position:fixed;bottom:80px;left:50%;transform:translateX(-50%);background:#3fb950;color:#080c18;padding:8px 16px;border-radius:8px;font-size:14px;font-weight:600;z-index:100">' + labels['toast'] + '</div>
<script>
''' + js_var + '''
function getShareData(){
  var meta=document.querySelector('meta[name="description"]');
  var ogImage=document.querySelector('meta[property="og:image"]');
  var canonical=document.querySelector('link[rel="canonical"]');
  var slug=window.location.pathname.replace(/^\//,'').replace(/index\.html$/,'').replace(/\.html$/,'');
  var shareUrl=canonical?canonical.href:window.location.origin+window.location.pathname.replace(/index\.html$/,'').replace(/\.html$/,'');
  var utm='?utm_source='+slug+'&utm_medium=social&utm_campaign=article_share';
  return{
    url:shareUrl+utm,
    rawUrl:window.location.href,
    slug:slug,
    title:document.title,
    desc:meta?meta.content:'',
    img:ogImage?ogImage.content:'',
    customText:__customShareText
  }
}
function truncate(str,maxLen){
  if(str.length<=maxLen)return str;
  return str.substring(0,maxLen-1)+'\u2026';
}
function shareToX(){
  var d=getShareData();
  var url=encodeURIComponent(d.url);
  var text;
  if(d.customText){
    text=encodeURIComponent(d.customText);
  }else{
    var title=d.title.replace(/ - FoneClaw$/,'');
    var maxText=255-title.length;
    var desc=maxText>20?truncate(d.desc,maxText):'';
    text=encodeURIComponent(title+(desc?'\\n\\n'+desc:''));
  }
  trackShare('x',d.slug);
  window.open("https://twitter.com/intent/tweet?url="+url+"&text="+text,"_blank","width=600,height=400")
}
function shareToTelegram(){
  var d=getShareData();
  var url=encodeURIComponent(d.url);
  var text;
  if(d.customText){
    text=encodeURIComponent(d.customText+'\\n\\n'+d.url);
  }else{
    text=encodeURIComponent(d.title+(d.desc?'\\n\\n'+d.desc:'')+'\\n\\n'+d.url);
  }
  trackShare('telegram',d.slug);
  window.open("https://t.me/share/url?url="+url+"&text="+text,"_blank","width=600,height=400")
}
function shareToLinkedIn(){
  var d=getShareData();
  var url=encodeURIComponent(d.url);
  var title=encodeURIComponent(d.title);
  var desc=encodeURIComponent(d.customText?truncate(d.customText,200):truncate(d.desc,200));
  trackShare('linkedin',d.slug);
  window.open("https://www.linkedin.com/sharing/share-offsite/?url="+url+"&title="+title+"&summary="+desc,"_blank","width=600,height=400")
}
function shareToFacebook(){
  var d=getShareData();
  trackShare('facebook',d.slug);
  window.open("https://www.facebook.com/sharer/sharer.php?u="+encodeURIComponent(d.url),"_blank","width=600,height=400")
}
function shareToReddit(){
  var d=getShareData();
  var url=encodeURIComponent(d.url);
  var title=encodeURIComponent(d.customText?truncate(d.customText,300):truncate(d.title,300));
  trackShare('reddit',d.slug);
  window.open("https://reddit.com/submit?url="+url+"&title="+title,"_blank","width=600,height=400")
}
function copyLink(){
  var d=getShareData();
  trackShare('copy_link',d.slug);
  navigator.clipboard.writeText(d.rawUrl).then(function(){
    var t=document.getElementById("copy-toast");
    t.style.display="block";
    setTimeout(function(){t.style.display="none"},2000)
  })
}
</script>
'''
    return (html
        .replace("title=\"' + labels['telegram'] + '\"", f"title=\"{labels['telegram']}\"")
        .replace("title=\"' + labels['linkedin'] + '\"", f"title=\"{labels['linkedin']}\"")
        .replace("title=\"' + labels['facebook'] + '\"", f"title=\"{labels['facebook']}\"")
        .replace("title=\"' + labels['reddit'] + '\"", f"title=\"{labels['reddit']}\"")
        .replace("title=\"' + labels['copy'] + '\"", f"title=\"{labels['copy']}\"")
        .replace("' + labels['toast'] + '", labels['toast'])
    )
