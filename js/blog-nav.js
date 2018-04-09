"use strict";

function ToggleShowTOC(e) {
  // prevent page from jumping to top when toc is toggled
  e.preventDefault();
  var nav = document.querySelector("nav");
  nav.classList.toggle("toc-shown");

  var body = document.querySelector("body");
  body.classList.toggle("toc-shown");
}

