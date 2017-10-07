var boxes = document.querySelectorAll("section.main aside");
for (var i = 0; i < boxes.length; ++i) {
  var box = boxes[i];
  box.addEventListener("click",
      function() {
        this.classList.toggle("selected");
      }
  );
}
