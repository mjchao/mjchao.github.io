"use strict";

function ToggleShowTOC(e) {
  // prevent page from jumping to top when toc is toggled
  e.preventDefault();
  var nav = document.querySelector("nav");
  nav.classList.toggle("toc-shown");

  var toc = document.querySelector(".toc");
  toc.style.maxHeight = (window.innerHeight - 64) + "px";
  console.log(toc.style.maxHeight);
}

