$(function () {
    $("#album").submit(function (e) {
        e.preventDefault();
        var data = new FormData(this);
        $.ajax({
            url: '/album/',
            cache: false,
            data: data,
            type: 'POST',
            processData: false,
            contentType: false,
            success: function (data) {

            }
        });
        return false;
    });



});