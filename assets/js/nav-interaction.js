/**
 * nav-interaction.js - Hamburger menu toggle and language selector dropdown
 * Pure vanilla JS, no dependencies. Use with <script defer src="/assets/js/nav-interaction.js"></script>
 *
 * Expected DOM structure:
 *   <button class="hamburger">...</button>
 *   <nav class="nr">...</nav>
 *   <button class="lang-toggle">...</button>
 *   <div class="lang-dropdown">...</div>
 */
(function(){
  "use strict";

  function init(){
    setupHamburger();
    setupLangSelector();
    syncLanguageSelectors();
    setupOutsideClick();
  }

  function setupHamburger(){
    var hamburger=document.querySelector(".hamburger");
    var nav=document.querySelector(".nr");
    if(!hamburger||!nav)return;

    hamburger.setAttribute("aria-expanded","false");
    hamburger.setAttribute("aria-label","Toggle menu");

    hamburger.addEventListener("click",function(e){
      e.stopPropagation();
      var isOpen=nav.classList.toggle("open");
      hamburger.classList.toggle("open");
      hamburger.setAttribute("aria-expanded",String(isOpen));

      // Prevent body scroll when menu is open
      if(isOpen){
        document.body.style.overflow="hidden";
      }else{
        document.body.style.overflow="";
      }
    });

    // Close on Escape
    document.addEventListener("keydown",function(e){
      if(e.key==="Escape"&&nav.classList.contains("open")){
        nav.classList.remove("open");
        hamburger.classList.remove("open");
        hamburger.setAttribute("aria-expanded","false");
        document.body.style.overflow="";
      }
    });
  }

  function syncLanguageSelectors(){
    var html=document.documentElement;
    var htmlLang=(html&&html.getAttribute("lang")||"en").toLowerCase();
    var normalizedHtmlLang=htmlLang.split("-")[0];

    document.querySelectorAll(".lang-sel").forEach(function(sel){
      var expected=(sel.getAttribute("data-lang")||normalizedHtmlLang||"en").toLowerCase();
      if(expected==="zh-tw") expected="tw";

      var match=Array.prototype.slice.call(sel.options).filter(function(opt){
        return (opt.getAttribute("data-lang")||"").toLowerCase()===expected;
      })[0];

      if(match&&sel.value!==match.value){
        sel.value=match.value;
      }
    });
  }

  function setupLangSelector(){
    var toggle=document.querySelector(".lang-toggle");
    var dropdown=document.querySelector(".lang-dropdown");
    if(!toggle||!dropdown)return;

    toggle.setAttribute("aria-expanded","false");
    toggle.setAttribute("aria-haspopup","true");

    toggle.addEventListener("click",function(e){
      e.stopPropagation();
      var isOpen=dropdown.classList.toggle("open");
      toggle.classList.toggle("open");
      toggle.setAttribute("aria-expanded",String(isOpen));
    });

    // Close dropdown when clicking a language option
    dropdown.querySelectorAll("a,button,[role='option']").forEach(function(opt){
      opt.addEventListener("click",function(){
        dropdown.classList.remove("open");
        toggle.classList.remove("open");
        toggle.setAttribute("aria-expanded","false");
      });
    });
  }

  function setupOutsideClick(){
    document.addEventListener("click",function(e){
      // Close hamburger nav if clicking outside
      var nav=document.querySelector(".nr");
      var hamburger=document.querySelector(".hamburger");
      if(nav&&nav.classList.contains("open")&&!nav.contains(e.target)&&!hamburger.contains(e.target)){
        nav.classList.remove("open");
        hamburger.classList.remove("open");
        hamburger.setAttribute("aria-expanded","false");
        document.body.style.overflow="";
      }

      // Close lang dropdown if clicking outside
      var dropdown=document.querySelector(".lang-dropdown");
      var langToggle=document.querySelector(".lang-toggle");
      if(dropdown&&dropdown.classList.contains("open")&&!dropdown.contains(e.target)&&!langToggle.contains(e.target)){
        dropdown.classList.remove("open");
        langToggle.classList.remove("open");
        langToggle.setAttribute("aria-expanded","false");
      }
    });
  }

  if(document.readyState==="loading"){
    document.addEventListener("DOMContentLoaded",init);
  }else{
    init();
  }

  // Browsers may restore <select> values from bfcache on Back/Forward.
  // Always resync the visible language selector to the current page language.
  window.addEventListener("pageshow",syncLanguageSelectors);
  window.addEventListener("popstate",syncLanguageSelectors);
})();
