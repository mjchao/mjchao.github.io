"use strict";

function BuildOnCloseButtonClicked(parent_box) {
  return function() {
    if (parent_box.classList.contains("selected")) {
      parent_box.classList.toggle("selected");
    }
  }
}

var boxes = document.querySelectorAll("section.main aside");
for (var i = 0; i < boxes.length; ++i) {
  var box = boxes[i];
  box.addEventListener("click",
    function(e) {
      if (!e.target.classList.contains("close") &&
          !this.classList.contains("selected")) {
        this.classList.toggle("selected");
      }
    }
  );

  var close_button = document.createElement("a");
  close_button.addEventListener("click", BuildOnCloseButtonClicked(box));
  close_button.className = "close";
  close_button.text = "\u00d7";
  box.insertBefore( close_button, box.childNodes[0] );
}
