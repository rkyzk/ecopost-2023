/** Bookmark buttons */

document.addEventListener("DOMContentLoaded", function () {
    let bmBtns = document.getElementsByClassName('bookmark');
    for (bmBtn of bmBtns) {
        bmBtn.addEventListener("click", function () {
            let csrftoken = getCookie('csrftoken');
            let url = 'bookmark/';
            let bMark = bmBtn.lastElementChild.classList.contains('fa-bookmark-o');
            $.ajax({
                url: url,
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: csrftoken,
                },
                success: function (response) {
                    // if BM button is clicked, fill in the icon
                    if (bMark) {
                        bmBtn.innerHTML = '<i class="fa fa-bookmark" aria-hidden="true"></i>';
                    } else {
                        // if unbookmark is clicked, show only the outline of the icon
                        bmBtn.innerHTML = '<i class="fa fa-bookmark-o" aria-hidden="true"></i>';
                    }
                },
                error: function (response) {
                    alert("Error occured.  Please try again.");
                }
            })
        });
    }
});