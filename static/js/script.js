// For small screen devices, clicking the hamburger icon will display the menu.
let open;
const menu = document.querySelector("#nav-menu");

function openMenu() {
    if (open) {
        menu.style.display = "none";
        open = false;
    } else if (!open) {
        menu.style.display = "block";
        open = true;
    }
}