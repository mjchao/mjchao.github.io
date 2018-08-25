function toggleCollapsedMenu() {
  var nav = document.getElementsByTagName("nav")[0];
  if (nav.className == "") {
    nav.className = "collapsed-showing";
  } else {
    nav.className = "";
  }
}
