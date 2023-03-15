var sidebar = document.getElementById("sidebar");
var body = document.getElementById("content");
var slide;
var sidebarWidth = "74px";
sidebar.style.width = sidebarWidth;
body.style.marginLeft = sidebarWidth;
sidebar.addEventListener("mouseover", function () {
    console.log("opening sidebar");
    if (window.innerWidth > 1200) {
        slide = "280px";
    }
    else if (window.innerWidth < 1201) {
        slide = "210px";
    }
    else if (window.innerWidth < 900) {
        slide = "160px";
    }
    else if (window.innerWidth < 800) {
        slide = "130px";
    }
    sidebar.style.width = slide;
    body.style.marginLeft = slide;
});
sidebar.addEventListener("mouseout", function () {
    console.log("closing sidebar");
    sidebar.style.width = sidebarWidth;
    body.style.marginLeft = sidebarWidth;
});
