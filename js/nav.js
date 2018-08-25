function toggleCollapsedMenu(e) {
  var nav = document.getElementsByTagName("nav")[0];
  if (nav.className == "") {
    nav.className = "collapsed-showing";
  } else {
    nav.className = "";
  }
  return false;
}
