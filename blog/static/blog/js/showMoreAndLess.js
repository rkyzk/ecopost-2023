/** functions for "Show more" and "Show less" buttons to work on 'My Page' */

document.addEventListener("DOMContentLoaded", function () {
    // Show more posts with show more button
    let button = document.getElementsByClassName('show-posts');
    for (btn of button) {
        btn.addEventListener("click", function () {
            let posts = this.nextElementSibling;
            if (this.classList.contains('show')) {
                this.classList.remove('show');
                this.classList.add('hide');
                posts.classList.remove('hide');
                posts.classList.add('show');
            }
        });
    }

    // Clicking 'Show less' button will hide posts.
    let hideButton = document.getElementsByClassName('hide-posts');
    for (hideBtn of hideButton) {
        hideBtn.addEventListener("click", function () {
            let posts = this.parentElement;
            posts.classList.remove('show');
            posts.classList.add('hide');
            // add 'show' to button 'show-posts'
            posts.previousElementSibling.classList.add('show');
            posts.previousElementSibling.classList.remove('hide');
        });
    }
});