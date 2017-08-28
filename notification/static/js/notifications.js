
$(function () {
  function check_notifications() {

    $.ajax({
      url: '/notifications/check/',
      cache: false,
      success: function (data) {
          $("#notifications").html(data);

        },
      complete: function () {
        window.setTimeout(check_notifications, 30000);
      }
    });
  };
  check_notifications();
});



$(function () {
  function count_notifications() {

    $.ajax({
      url: '/notifications/count/',
      cache: false,
      success: function (data) {

      if (data>0){
          $("#count").text(data).show();

        }
        },
      complete: function () {
        window.setTimeout(count_notifications, 30000);
      }
    });
  };
  count_notifications();
});