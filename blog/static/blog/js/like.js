/** like and unlike buttons */

document.addEventListener("DOMContentLoaded", function () {
    // post like & unlike
    let likeBtns = document.getElementsByClassName('like-btn');
    for (likeBtn of likeBtns) {
        likeBtn.addEventListener("click", function () {
            let csrftoken = getCookie('csrftoken');
            let url = 'post_like/';
            let likesCount = parseInt(likeBtn.nextElementSibling.textContent);
            let like = likeBtn.lastElementChild.classList.contains('fa-regular');
            $.ajax({
                url: url,
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: csrftoken,
                },
                success: function (response) {
                    // if like button is clicked, fill in the heart and add 1 to the count
                    if (like) {
                        likeBtn.innerHTML = '<i class="fa-solid fa-heart heart"></i>';
                        likeBtn.nextElementSibling.textContent = likesCount + 1;
                    } else {
                        // if unlike is clicked, show only the heart outline and subtract 1
                        // from the likes count.
                        likeBtn.innerHTML = '<i class="fa-regular fa-heart heart"></i>';
                        likeBtn.nextElementSibling.textContent = likesCount - 1;
                    }
                },
                error: function (response) {
                    alert("Error occured.  Please try again.");
                }
            })
        });
    }
});