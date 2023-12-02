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

/** get updated comments that users entered, and send a request to save them. */
$(document).on('submit', '#save-comment-form', function (e) {
    e.preventDefault();
    let csrftoken = getCookie('csrftoken');
    let id = this.dataset.id;
    let url = 'update_comment/';
    /** get the input from user */
    let comment = document.getElementById("comment").value;
    /** comment before update */
    var originalCmmt = document.getElementById("save-cmmt-btn").value;
    var validation = this.previousElementSibling;
    var editedLabel = validation.parentElement.previousElementSibling.previousElementSibling;
    // if input is empty, display a note 'Please enter this field'
    if (comment.trim() === "") {
        validation.classList.remove('hide');
        validation.classList.add('show');
    } else {
        // get edit and delete icons
        let commentParent = this.parentElement;
        let icons = commentParent.nextElementSibling;
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
                // if the note 'Please enter this field' is displayed, hide it.
                if (validation.classList.contains('show')) {
                    validation.classList.remove('show');
                    validation.classList.add('hide');
                }
                // if 'edited' label is absent, display it until the next page refresh
                if (editedLabel.textContent != 'edited') {
                    editedLabel.nextElementSibling.classList.remove('hide');
                    editedLabel.nextElementSibling.classList.add('show');
                }
            },
            error: function (response) {
                alert("Error occured.  Your comment wasn't saved.");
                commentParent.textContent = originalCmmt;
            },
            complete: function (response) {
                icons.classList.remove('d-none');
                icons.classList.add('d-flex');
            }
        })
    }
});