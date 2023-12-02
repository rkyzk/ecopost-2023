/**
 * For small screen devices, open and close the burger menu
 */

/** if 'open' is true, the menu is open */
let open;

/** get the nav menu */
const menu = document.querySelector("#nav-menu");

/** close the menu */
const closeMenu = () => {
    setTimeout(function () {
        menu.style.display = "none";
        open = false;
        document.removeEventListener('mouseup', closeMenu)
    }, 100);
};

/** open the menu */
const openMenu = () => {
    if (open) {
        menu.style.display = "none";
        open = false;
    } else {
        menu.style.display = "block";
        open = true;
        document.addEventListener('mouseup', closeMenu)
    }
};