/**
 * back-to-top.js - Show/hide back-to-top button based on scroll position
 * Pure vanilla JS, no dependencies. Use with <script defer src="/assets/js/back-to-top.js"></script>
 *
 * Expected DOM: <button id="backToTop">...</button>
 * The button is injected if not found, with a built-in chevron SVG.
 */
(function(){
  "use strict";

  var THRESHOLD=400;
  var BTN_ID="backToTop";

  function init(){
    var btn=document.getElementById(BTN_ID);
    if(!btn){
      btn=createButton();
      document.body.appendChild(btn);
    }

    // Initial state
    btn.style.opacity="0";
    btn.style.visibility="hidden";

    // Scroll handler
    var ticking=false;
    window.addEventListener("scroll",function(){
      if(!ticking){
        requestAnimationFrame(function(){
          if(window.scrollY>THRESHOLD){
            btn.style.opacity="1";
            btn.style.visibility="visible";
          }else{
            btn.style.opacity="0";
            btn.style.visibility="hidden";
          }
          ticking=false;
        });
        ticking=true;
      }
    },{passive:true});

    // Click handler
    btn.addEventListener("click",function(e){
      e.preventDefault();
      window.scrollTo({top:0,behavior:"smooth"});
    });
  }

  function createButton(){
    var btn=document.createElement("button");
    btn.id=BTN_ID;
    btn.title="Back to top";
    btn.setAttribute("aria-label","Back to top");
    btn.style.cssText="position:fixed;bottom:24px;right:24px;width:44px;height:44px;border-radius:50%;background:#0d1117;border:1px solid #21262d;color:#8b949e;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:9998;transition:opacity .3s,visibility .3s,background .2s,color .2s";
    btn.innerHTML='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>';

    btn.addEventListener("mouseenter",function(){
      btn.style.background="#161b22";
      btn.style.color="#c9d1d9";
    });
    btn.addEventListener("mouseleave",function(){
      btn.style.background="#0d1117";
      btn.style.color="#8b949e";
    });

    return btn;
  }

  if(document.readyState==="loading"){
    document.addEventListener("DOMContentLoaded",init);
  }else{
    init();
  }
})();
