/** Show and hide comment edit forms */

/** hide comment edit form */
const hideForm = (event) => {
    let comment = event.parentElement.parentElement.parentElement;
    let textBox = event.parentElement.previousElementSibling;
    let icons = comment.nextElementSibling;
    icons.classList.remove('d-none');
    icons.classList.add('d-flex');
    comment.innerText = textBox.textContent;
}

/** get comments and display comment edit form */
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
    let comment = icons.previousElementSibling;
    var content = comment.textContent;
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            id: id
        },
        success: function (response) {
            content = response['content'];
            let commentBox = `
                <span id="comment-validation" class="hide" style="color: red;">
                  Please enter this field.
                </span>
                <form class="d-flex" id="save-comment-form" data-id=${id} method="POST">
                  <textarea type="text" class="update-form" id="comment">${content}</textarea>
                  <div>
                    <button class="blue-btn" type="submit" value="${content}"
                      id="save-cmmt-btn">save</button>
                    <button class="blue-btn mt-1" onClick="hideForm(this)">
                      cancel
                    </button>
                  </div>
                </form>
                `;
            comment.innerHTML = commentBox;
            $('#comment').focus();
        },
        error: function (response) {
            alert("error getting data");
            // Display the original comment and icons
            comment.textContent = content;
        },
        complete: function (response) {
            icons.classList.remove("d-none");
            icons.classList.add("d-flex");
        }
    })
}