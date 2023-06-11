/************** Hide Navbar When Scroll **************/

var firstScrollPosition = window.pageYOffset;                       //Assigns page height to 'firstScrollPosition'
window.onscroll = function () {
    var currentScrollPosition = window.pageYOffset;
    if (firstScrollPosition > currentScrollPosition) {
        document.getElementById("navbar").style.top = "0";      //Shows navbar
    } else {
        document.getElementById("navbar").style.top = "-60px";  //Hides Navbar
    }
    firstScrollPosition = currentScrollPosition;            //Update scroll position
}

/************** Hide Navbar When Scroll **************/