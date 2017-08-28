$(function () {
  $("#send").submit(function () {
    $.ajax({
      url: '/messages/send/',
      data: $("#send").serialize(),
      cache: false,
      type: 'post',
      success: function (data) {
        $(".scroll").append(data);
        $(".msg_container_base0").stop().animate({ scrollTop: $(".msg_container_base0")[0].scrollHeight}, 0);

      }

    });

    return false;
  });



});


$(function(){
    $('#upload-image-form').submit(function(){
        $.ajax({
            url : '/messages/send1/',
            data : new FormData(this),
            type : 'POST',
            cache : false,
            processData: false,
            contentType: false,
            success : function(data){
          $(".scroll").append(data);
         $(".msg_container_base0").stop().animate({ scrollTop: $(".msg_container_base0")[0].scrollHeight}, 0);

            }
        });
        return false ;

   });


});
