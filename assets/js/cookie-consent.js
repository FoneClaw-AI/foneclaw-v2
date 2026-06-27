/**
 * cookie-consent.js - Multilingual cookie consent banner with localStorage persistence
 * Pure vanilla JS, no dependencies.
 */
(function(){
  "use strict";

  var STORAGE_KEY="foneclaw_cookie_consent";
  var BANNER_ID="__fc_cookie_consent";

  var I18N={
    en:{text:"This site uses cookies to enhance your experience. By continuing to visit this site you agree to our use of cookies.",learn:"Learn more",accept:"Accept"},
    zh:{text:"本网站使用 Cookie 来提升您的体验。继续访问即表示您同意我们使用 Cookie。",learn:"了解更多",accept:"接受"},
    tw:{text:"本網站使用 Cookie 來提升您的體驗。繼續造訪即表示您同意我們使用 Cookie。",learn:"了解更多",accept:"接受"},
    ja:{text:"このサイトはCookieを使用してエクスペリエンスを向上させています。アクセスを続けることでCookieの使用に同意したものとみなされます。",learn:"詳細",accept:"同意する"},
    ko:{text:"이 사이트는 사용자 경험 향상을 위해 쿠키를 사용합니다. 계속 방문하면 쿠키 사용에 동의하는 것으로 간주됩니다.",learn:"자세히 보기",accept:"수락"},
    es:{text:"Este sitio utiliza cookies para mejorar su experiencia. Al continuar visitando este sitio, usted acepta nuestro uso de cookies.",learn:"Mas informacion",accept:"Aceptar"},
    pt:{text:"Este site usa cookies para melhorar sua experiencia. Ao continuar visitando este site, voce concorda com nosso uso de cookies.",learn:"Saiba mais",accept:"Aceitar"},
    ru:{text:"Этот сайт использует файлы cookie для улучшения вашего опыта. Продолжая посещение, вы соглашаетесь с использованием cookie.",learn:"Подробнее",accept:"Принять"},
    fr:{text:"Ce site utilise des cookies pour ameliorer votre experience. En continuant a visiter ce site, vous acceptez notre utilisation des cookies.",learn:"En savoir plus",accept:"Accepter"},
    de:{text:"Diese Website verwendet Cookies, um Ihr Erlebnis zu verbessern. Durch die weitere Nutzung stimmen Sie der Verwendung von Cookies zu.",learn:"Mehr erfahren",accept:"Akzeptieren"},
    ar:{text:"يستخدم هذا الموقع ملفات الارتباط لتحسين تجربتك. بالاستمرار في زيارة هذا الموقع، فإنك توافق على استخدامنا لملفات الارتباط.",learn:"اعرف المزيد",accept:"قبول"},
    th:{text:"เว็บไซต์นี้ใช้คุกกี้เพื่อปรับปรุงประสบการณ์ของคุณ การเข้าชมต่อแสดงว่าคุณยอมรับการใช้คุกกี้ของเรา",learn:"เรียนรู้เพิ่มเติม",accept:"ยอมรับ"},
    vi:{text:"Trang web nay su dung Cookie de cai thien trai nghiem cua ban. Tiep tuc truy cap dong nghia voi viec ban dong y su dung Cookie.",learn:"Tim hieu them",accept:"Chap nhan"},
    id:{text:"Situs ini menggunakan Cookie untuk meningkatkan pengalaman Anda. Dengan melanjutkan kunjungan, Anda menyetujui penggunaan Cookie kami.",learn:"Pelajari lebih lanjut",accept:"Terima"}
  };

  function hasConsented(){
    try{return localStorage.getItem(STORAGE_KEY)==="accepted";}
    catch(e){return false;}
  }

  function saveConsent(){
    try{localStorage.setItem(STORAGE_KEY,"accepted");}
    catch(e){}
  }

  function dismissBanner(){
    var banner=document.getElementById(BANNER_ID);
    if(!banner)return;
    banner.style.opacity="0";
    banner.style.transform="translateY(100%)";
    setTimeout(function(){
      if(banner.parentNode)banner.parentNode.removeChild(banner);
    },400);
  }

  function getLang(){
    var html=document.documentElement;
    var lang=html.getAttribute("lang")||"en";
    // Normalize: zh-CN->zh, zh-TW->tw, ja-JP->ja, etc.
    lang=lang.toLowerCase().split("-")[0];
    if(lang==="zh"){
      // Check if Traditional Chinese (tw dir or zh-TW)
      if(html.getAttribute("dir")==="tw"||html.lang.indexOf("TW")!==-1) return "tw";
      return "zh";
    }
    return I18N[lang]?lang:"en";
  }

  function getCookiePath(lang){
    if(lang==="en") return "/cookie.html";
    return "/"+lang+"/cookie.html";
  }

  function createBanner(){
    if(hasConsented())return;
    if(document.getElementById(BANNER_ID))return;

    var lang=getLang();
    var t=I18N[lang]||I18N.en;
    var isRTL=lang==="ar";

    var banner=document.createElement("div");
    banner.id=BANNER_ID;
    banner.setAttribute("role","dialog");
    banner.setAttribute("aria-label","Cookie consent");
    banner.style.cssText="position:fixed;bottom:0;left:0;right:0;z-index:10001;background:#161b22;border-top:1px solid #30363d;padding:16px 20px;display:flex;align-items:center;justify-content:center;gap:16px;flex-wrap:wrap;transition:opacity .4s,transform .4s;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"+(isRTL?";direction:rtl":"");

    var textSpan=document.createElement("span");
    textSpan.style.cssText="color:#8b949e;font-size:14px;line-height:1.5;max-width:600px";
    textSpan.textContent=t.text+" ";

    var learnLink=document.createElement("a");
    learnLink.href=getCookiePath(lang);
    learnLink.textContent=t.learn;
    learnLink.style.cssText="color:#00d4ff;text-decoration:underline;font-size:14px;white-space:nowrap";

    var btn=document.createElement("button");
    btn.textContent=t.accept;
    btn.style.cssText="background:#3fb950;color:#080c18;border:none;padding:8px 20px;border-radius:6px;font-size:14px;font-weight:600;cursor:pointer;transition:background .2s;white-space:nowrap";

    btn.addEventListener("mouseenter",function(){btn.style.background="#56d364";});
    btn.addEventListener("mouseleave",function(){btn.style.background="#3fb950";});

    btn.addEventListener("click",function(e){
      e.preventDefault();
      saveConsent();
      dismissBanner();
    });

    textSpan.appendChild(learnLink);
    banner.appendChild(textSpan);
    banner.appendChild(btn);
    document.body.appendChild(banner);

    requestAnimationFrame(function(){
      banner.style.opacity="1";
      banner.style.transform="translateY(0)";
    });
  }

  if(document.readyState==="loading"){
    document.addEventListener("DOMContentLoaded",createBanner);
  }else{
    createBanner();
  }
})();
