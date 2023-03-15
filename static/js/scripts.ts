const sidebar = document.getElementById("sidebar")
const body = document.getElementById("content")
let slide: string
let sidebarWidth: string = "74px"

sidebar.style.width = sidebarWidth
body.style.marginLeft = sidebarWidth

sidebar.addEventListener("mouseover", () => {
    console.log("opening sidebar")

    if (window.innerWidth > 1200) {
        slide = "280px"
    } else if (window.innerWidth < 1201) {
        slide = "210px"
    }
    else if (window.innerWidth < 900) {
        slide = "160px"
    }
    else if (window.innerWidth < 800) {
        slide = "130px"
    }

    sidebar.style.width = slide
    body.style.marginLeft = slide
});

sidebar.addEventListener("mouseout", () => {
    console.log("closing sidebar")
    sidebar.style.width = sidebarWidth
    body.style.marginLeft = sidebarWidth
});
