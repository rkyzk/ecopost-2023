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

document.addEventListener("DOMContentLoaded", function () {
    // Show more posts with show more button
    let button = document.getElementsByClassName('show-posts');
    for (btn of button) {
        btn.addEventListener("click", function () {
            let posts = this.nextElementSibling;
            if (this.textContent == 'Show more') {
                this.textContent = 'Show less'
                posts.classList.remove('hide');
                posts.classList.add('show');
            } else {
                this.textContent = 'Show more'
                posts.classList.remove('show');
                posts.classList.add('hide');
            }
        });
    }

    // Clicking 'Show less' button will hide posts.
    let hideButton = document.getElementsByClassName('hide-posts');
    for (hideBtn of hideButton) {
        hideBtn.addEventListener("click", function () {
            let posts = this.parentElement;
            posts.previousElementSibling.textContent = 'Show more'
            posts.classList.remove('show');
            posts.classList.add('hide');
        });
    }
});