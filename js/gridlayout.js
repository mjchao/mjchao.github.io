"use strict";

var boxes = document.querySelectorAll("section.main aside");
for (var i = 0; i < boxes.length; ++i) {
  var box = boxes[i];
  box.addEventListener("click",
    function() {
      this.classList.toggle("selected");
    }
  );

  var close_button = document.createElement("a");
  close_button.className = "close btn";
  close_button.text = "close";
  box.insertBefore( close_button, box.childNodes[0] );
}
