document.addEventListener("DOMContentLoaded", function () {
    // Let messages appear for 4 seconds
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 4000);
});