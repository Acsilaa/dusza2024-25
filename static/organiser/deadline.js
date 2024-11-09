$(function () {
    document.getElementById("deadline").min = new Date().toISOString().substring(0, 16);
})