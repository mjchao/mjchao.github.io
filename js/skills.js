function hasClass( elem, klass ) {
       return (" " + elem.className + " " ).indexOf( " "+klass+" " ) > -1;
}

var skill_boxes = document.querySelectorAll("section.main aside");
console.log(skill_boxes);
for (var i = 0; i < skill_boxes.length; ++i) {
  var skill_box = skill_boxes[i];
  skill_box.addEventListener("click",
      function() {
        this.classList.toggle("selected");
      }
  );
}
