/**
 * lazy-load.js - IntersectionObserver-based lazy loading for images with data-src
 * Pure vanilla JS, no dependencies. Use with <script defer src="/assets/js/lazy-load.js"></script>
 *
 * Usage: <img data-src="/path/to/image.jpg" alt="..." class="lazy">
 * On intersection, sets src from data-src and removes the lazy marker.
 */
(function(){
  "use strict";

  var SELECTOR="img[data-src]";

  function loadImage(img){
    var src=img.getAttribute("data-src");
    if(!src)return;
    img.src=src;
    img.removeAttribute("data-src");
    img.classList.remove("lazy");
    img.classList.add("lazy-loaded");
  }

  function initGifHover(){
    var gifs=document.querySelectorAll("img.lazy-gif[data-gif]");
    gifs.forEach(function(img){
      if(img.dataset.gifHoverBound==="1")return;
      img.dataset.gifHoverBound="1";
      var poster=img.getAttribute("src");
      var gif=img.getAttribute("data-gif");
      if(!gif)return;
      function play(){ img.src=gif; img.dataset.gifPlaying="1"; }
      function stop(){ img.src=poster; img.dataset.gifPlaying="0"; }
      function toggle(){ img.dataset.gifPlaying==="1" ? stop() : play(); }
      if(window.matchMedia && window.matchMedia("(hover: hover)").matches){
        img.addEventListener("mouseenter",play);
        img.addEventListener("mouseleave",stop);
      }else{
        img.addEventListener("click",function(e){ e.preventDefault(); toggle(); });
      }
    });
  }

  function init(){
    initGifHover();

    var images=document.querySelectorAll(SELECTOR);
    if(!images.length)return;

    // Fallback for browsers without IntersectionObserver
    if(!("IntersectionObserver" in window)){
      images.forEach(loadImage);
      return;
    }

    var observer=new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          var img=entry.target;
          loadImage(img);
          observer.unobserve(img);
        }
      });
    },{
      rootMargin:"200px 0px",
      threshold:0.01
    });

    images.forEach(function(img){
      observer.observe(img);
    });
  }

  if(document.readyState==="loading"){
    document.addEventListener("DOMContentLoaded",init);
  }else{
    init();
  }
})();
