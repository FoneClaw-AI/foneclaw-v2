/**
 * social-share.js - Renders share buttons from social.json into #social-share
 * Pure vanilla JS, no dependencies. Use with <script defer src="/assets/js/social-share.js"></script>
 */
(function(){
  "use strict";

  var TOAST_ID="__fc_copy_toast";
  var SHARE_DATA_ATTR="__fc_share_data";

  function getShareData(){
    var meta=document.querySelector('meta[name="description"]');
    var canonical=document.querySelector('link[rel="canonical"]');
    var slug=window.location.pathname.replace(/^\//,'').replace(/index\.html$/,'').replace(/\.html$/,'');
    var shareUrl=canonical?canonical.href:window.location.origin+window.location.pathname.replace(/index\.html$/,'').replace(/\.html$/,'');
    var utm='?utm_source='+slug+'&utm_medium=social&utm_campaign=article_share';
    return{
      url:shareUrl+utm,
      rawUrl:window.location.href,
      slug:slug,
      title:document.title,
      desc:meta?meta.content:''
    };
  }

  function truncate(str,maxLen){
    if(str.length<=maxLen)return str;
    return str.substring(0,maxLen-1)+'\u2026';
  }

  // X/Twitter counts tweet length with weighted characters and every URL as a fixed t.co URL.
  // As of current X rules, HTTPS URLs count as 23 characters, no matter how long the raw URL is.
  // CJK characters generally count as 2 weighted chars. Keep a safety margin below 280.
  var X_MAX_WEIGHT=260;
  var X_URL_WEIGHT=23;

  function xCharWeight(ch){
    var cp=ch.codePointAt(0);
    if(cp>0xFFFF)return 2; // emoji/surrogate pair safety
    if((cp>=0x1100&&cp<=0x11FF)||(cp>=0x2E80&&cp<=0xA4CF)||(cp>=0xAC00&&cp<=0xD7AF)||(cp>=0xF900&&cp<=0xFAFF)||(cp>=0xFE10&&cp<=0xFE6F)||(cp>=0xFF00&&cp<=0xFFEF))return 2;
    return 1;
  }

  function xWeightedLength(str){
    var total=0;
    for(var i=0;i<str.length;i++){
      var ch=str[i];
      var cp=ch.codePointAt(0);
      total+=xCharWeight(ch);
      if(cp>0xFFFF)i++;
    }
    return total;
  }

  function truncateXWeighted(str,maxWeight){
    if(xWeightedLength(str)<=maxWeight)return str;
    var out='', used=0, ell='\u2026', ellW=xWeightedLength(ell);
    for(var i=0;i<str.length;i++){
      var ch=str[i];
      var cp=ch.codePointAt(0);
      if(cp>0xFFFF){ch=str.substring(i,i+2);}
      var w=xCharWeight(ch);
      if(used+w+ellW>maxWeight)break;
      out+=ch; used+=w;
      if(cp>0xFFFF)i++;
    }
    return out+ell;
  }

  function buildXText(title,desc){
    var budget=X_MAX_WEIGHT-X_URL_WEIGHT-1; // text + space + t.co URL
    var cleanTitle=title.replace(/ - FoneClaw$/,'').trim();
    var cleanDesc=(desc||'').trim();
    if(xWeightedLength(cleanTitle)>budget)return truncateXWeighted(cleanTitle,budget);
    var prefix=cleanTitle;
    if(!cleanDesc)return prefix;
    var sep='\n\n';
    var remaining=budget-xWeightedLength(prefix)-xWeightedLength(sep);
    if(remaining<24)return prefix;
    return prefix+sep+truncateXWeighted(cleanDesc,remaining);
  }

  function createToast(){
    if(document.getElementById(TOAST_ID))return;
    var t=document.createElement("div");
    t.id=TOAST_ID;
    t.textContent="Link copied!";
    t.style.cssText="display:none;position:fixed;bottom:80px;left:50%;transform:translateX(-50%);background:#3fb950;color:#080c18;padding:8px 16px;border-radius:8px;font-size:14px;font-weight:600;z-index:10000;transition:opacity .3s";
    document.body.appendChild(t);
  }

  function showToast(){
    var t=document.getElementById(TOAST_ID);
    if(!t)return;
    t.style.display="block";
    t.style.opacity="1";
    setTimeout(function(){t.style.display="none";},2000);
  }

  function shareToX(){
    var d=getShareData();
    var url=encodeURIComponent(d.url);
    var text=encodeURIComponent(buildXText(d.title,d.desc));
    window.open("https://twitter.com/intent/tweet?url="+url+"&text="+text,"_blank","width=600,height=400");
  }

  function shareToTelegram(){
    var d=getShareData();
    var url=encodeURIComponent(d.url);
    var text=encodeURIComponent(d.title+(d.desc?'\n\n'+d.desc:'')+'\n\n'+d.url);
    window.open("https://t.me/share/url?url="+url+"&text="+text,"_blank","width=600,height=400");
  }

  function shareToLinkedIn(){
    var d=getShareData();
    var url=encodeURIComponent(d.url);
    var title=encodeURIComponent(d.title);
    var desc=encodeURIComponent(truncate(d.desc,200));
    window.open("https://www.linkedin.com/sharing/share-offsite/?url="+url+"&title="+title+"&summary="+desc,"_blank","width=600,height=400");
  }

  function shareToFacebook(){
    var d=getShareData();
    window.open("https://www.facebook.com/sharer/sharer.php?u="+encodeURIComponent(d.url),"_blank","width=600,height=400");
  }

  function shareToReddit(){
    var d=getShareData();
    var url=encodeURIComponent(d.url);
    var title=encodeURIComponent(truncate(d.title,300));
    window.open("https://reddit.com/submit?url="+url+"&title="+title,"_blank","width=600,height=400");
  }

  function copyLink(){
    var d=getShareData();
    navigator.clipboard.writeText(d.rawUrl).then(function(){
      showToast();
    }).catch(function(){
      var ta=document.createElement("textarea");
      ta.value=d.rawUrl;
      ta.style.position="fixed";
      ta.style.left="-9999px";
      document.body.appendChild(ta);
      ta.select();
      document.execCommand("copy");
      document.body.removeChild(ta);
      showToast();
    });
  }

  var handlers={
    x:shareToX,
    telegram:shareToTelegram,
    linkedin:shareToLinkedIn,
    facebook:shareToFacebook,
    reddit:shareToReddit,
    copy:copyLink
  };

  function renderButtons(platforms){
    var container=document.getElementById("social-share");
    if(!container)return;
    createToast();

    var btnCSS="width:40px;height:40px;border-radius:50%;background:#0d1117;border:1px solid #21262d;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;color:#8b949e;text-decoration:none";
    var hoverIn="background:#161b22;color:#c9d1d9;border-color:#30363d";
    var hoverOut="background:#0d1117;color:#8b949e;border-color:#21262d";

    container.style.cssText="position:fixed;right:20px;top:120px;z-index:9999;display:flex;flex-direction:column;gap:8px";

    platforms.forEach(function(p){
      var btn=document.createElement("button");
      btn.title=p.name;
      btn.style.cssText=btnCSS;
      btn.innerHTML=p.icon_svg;

      btn.addEventListener("mouseenter",function(){btn.style.cssText=btnCSS+";"+hoverIn;});
      btn.addEventListener("mouseleave",function(){btn.style.cssText=btnCSS+";"+hoverOut;});

      var handler=handlers[p.id];
      if(handler){
        btn.addEventListener("click",function(e){
          e.preventDefault();
          handler();
        });
      }
      container.appendChild(btn);
    });
  }

  function init(){
    var data=window.__FC_SOCIAL_DATA;
    if(data&&data.platforms){
      renderButtons(data.platforms);
    }else{
      console.warn("[social-share] No social data found");
    }
  }

  if(document.readyState==="loading"){
    document.addEventListener("DOMContentLoaded",init);
  }else{
    init();
  }
})();
