// For small screen devices, clicking the hamburger icon will display the menu.
let open;
const menu = document.querySelector("#nav-menu");

const closeMenu = () => {
    setTimeout(function () {
        menu.style.display = "none";
        open = false;
        document.removeEventListener('mouseup', closeMenu)
    }, 100);
}

const openMenu = () => {
    if (open) {
        menu.style.display = "none";
        open = false;
    } else {
        menu.style.display = "block";
        open = true;
        document.addEventListener('mouseup', closeMenu)
    }
}

// hide comment edit form
const hideForm = (event) => {
    let comment = event.parentElement.parentElement.parentElement;
    let textBox = event.parentElement.previousElementSibling;
    let icons = comment.nextElementSibling;
    icons.classList.remove('hide');
    icons.classList.add('d-flex');
    icons.classList.add('show');
    comment.innerText = textBox.textContent;
}

// display comments to be updated
showCommentEditForm = (event) => {
    // if another comment edit form is open, hide it
    let shownForm = document.getElementById('save-comment-form');
    if (shownForm) {
        let cancelBtn = shownForm.lastElementChild.lastElementChild;
        hideForm(cancelBtn);
    }
    let id = event.dataset.id;
    let url = 'get_comment/';
    let icons = event.parentElement.parentElement;
    icons.classList.remove('show');
    icons.classList.remove('d-flex');
    icons.classList.add('hide');
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            id: id
        },
        success: function (response) {
            var content = response['content'];
            let comment = icons.previousElementSibling;
            let commentBox = '<span id="comment-validation" class="hide" style="color: red;">' +
                'Please enter this field.</span>' +
                '<form class="d-flex" id="save-comment-form" data-id=' +
                id + ' method="POST"><textarea type="text"' +
                ' class="update-form" id="comment">' +
                content + '</textarea><div>' +
                '<button class="blue-btn" type="submit">save</button>' +
                '<button class="blue-btn mt-1" onClick="hideForm(this)">' +
                'cancel</button></div></form>';
            comment.innerHTML = commentBox;
            $('#comment').focus();
        },
        error: function (response) {
            alert("error getting data");
        }
    })
}

// The following function getCookie was copied from 
// https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// save updated comments
$(document).on('submit', '#save-comment-form', function (e) {
    e.preventDefault();
    let csrftoken = getCookie('csrftoken');
    let id = this.dataset.id;
    let url = 'update_comment/';
    let comment = document.getElementById("comment").value;
    let validation = this.previousElementSibling;
    // if input is empty, display a note 'Please enter this field'
    if (comment.trim() === "") {
        validation.classList.remove('hide');
        validation.classList.add('show');
    } else {
        // if the note 'Please enter this field' is displayed, hide it.
        if (validation.classList.contains('show')) {
            validation.classList.remove('show');
            validation.classList.add('hide');
        }
        // get edit and delete icons
        let commentParent = this.parentElement;
        let icons = commentParent.nextElementSibling;
        // if 'edited' label is absent, display it until the next page refresh
        let editedLabel = validation.parentElement.previousElementSibling;
        if (editedLabel.previousElementSibling.textContent !== 'edited') {
            editedLabel.classList.remove('hide');
            editedLabel.classList.add('show');
        }
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                id: id,
                comment: comment,
                csrfmiddlewaretoken: csrftoken,
            },
            success: function (response) {
                commentParent.textContent = comment;
                icons.classList.remove('hide');
                icons.classList.add('d-flex');
                icons.classList.add('show');
            },
            error: function (response) {
                alert("Error occured.  Your comment wasn't saved.");
            }
        })
    }
});

document.addEventListener("DOMContentLoaded", function () {
    // Let messages appear for 4 seconds
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 4000);

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