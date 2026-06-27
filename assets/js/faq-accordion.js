/**
 * faq-accordion.js - FAQ accordion with single-open behavior
 * Pure vanilla JS, no dependencies. Use with <script defer src="/assets/js/faq-accordion.js"></script>
 */
(function(){
  "use strict";

  function init(){
    var items=document.querySelectorAll(".faq-item");
    if(!items.length)return;

    items.forEach(function(item){
      var header=item.querySelector(".faq-question")||item.querySelector("h3")||item.querySelector("summary")||item.firstElementChild;
      if(!header)return;

      header.style.cursor="pointer";
      header.setAttribute("role","button");
      header.setAttribute("tabindex","0");
      header.setAttribute("aria-expanded","false");

      header.addEventListener("click",function(e){
        e.preventDefault();
        toggleItem(item,items);
      });

      header.addEventListener("keydown",function(e){
        if(e.key==="Enter"||e.key===" "){
          e.preventDefault();
          toggleItem(item,items);
        }
      });
    });
  }

  function toggleItem(item,allItems){
    var isOpen=item.classList.contains("open");

    // Close all
    allItems.forEach(function(i){
      i.classList.remove("open");
      var h=i.querySelector(".faq-question")||i.querySelector("h3")||i.querySelector("summary")||i.firstElementChild;
      if(h)h.setAttribute("aria-expanded","false");
    });

    // Toggle clicked
    if(!isOpen){
      item.classList.add("open");
      var header=item.querySelector(".faq-question")||item.querySelector("h3")||item.querySelector("summary")||item.firstElementChild;
      if(header)header.setAttribute("aria-expanded","true");
    }
  }

  if(document.readyState==="loading"){
    document.addEventListener("DOMContentLoaded",init);
  }else{
    init();
  }
})();
