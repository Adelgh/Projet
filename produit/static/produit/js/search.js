$(function () {
    $(".users-results li").click(function () {
        var feed = $(this).attr("user-id");
        location.href = "/user/";
    });
});