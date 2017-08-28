$(function () {
  $("#post").submit(function (e) {
  e.preventDefault();
   var  data = new FormData(this);
    $.ajax({
      url: '/post/post/',
      cache: false,
      data :data ,
      type: 'POST',
      processData : false,
      contentType : false,
      success: function (data) {
        $(".scroll").prepend(data);
 $( '.newsletterform' ).each(function(){
    this.reset();
});
}
  });
    return false;
  });
    $(".product").on('submit', '#comment', function (e) {
  e.preventDefault();
  var $this = $(this);
   var  data = new FormData(this);
   var postId = $(this).attr('data-post-id');

    $.ajax({
      url: '/post/comment/' + postId,
      cache: false,
      data :data ,
      type: 'POST',
      processData : false,
      contentType : false,
      success: function (data) {

        $this.siblings(".scrollbarr").prepend(data);
    $( '.newsletterform' ).each(function(){
    this.reset();
});
      }
  });
    return false;
  });
});

$(function(){

$('.post-form-button').click(function(){
$('.post-form').slideToggle()

});

});