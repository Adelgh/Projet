$(function () {

  $.ajaxSetup({
       beforeSend: function(xhr, settings) {
           function getCookie(name) {
               var cookieValue = null;
               if (document.cookie && document.cookie != '') {
                   var cookies = document.cookie.split(';');
                   for (var i = 0; i < cookies.length; i++) {
                       var cookie = jQuery.trim(cookies[i]);
                       // Does this cookie string begin with the name we want?
                       if (cookie.substring(0, name.length + 1) == (name + '=')) {
                           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                           break;
                       }
                   }
               }
               return cookieValue;
           }
           if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
               // Only send the token to relative URLs i.e. locally.
               xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
           }
       }
  });

    $('.reaction-button').on('click', function () {
      var $this = $(this);
      var type = $this.attr('data-reaction');
      var id = $this.attr('data-id');
      $.ajax({
          url: '/react/' + id,
          data: {
              'reaction': type

          },
          success: function (data) {
              if (data.count > 0) {
                  if (data.count > 1) {
                      $this.parent().siblings('.reactions').text(data.count + ' ' + ' like');

                  } else {
                      $this.parent().siblings('.reactions').text(data.count + ' ' + ' like');
                  }
              } else {
                  $this.parent().siblings('.reactions').text('');

              }
          }
      })
    });


$('.reaction-post').on('click', function () {
      var $this = $(this);
      var type = $this.attr('data-reaction');
      var id = $this.attr('data-id');
      $.ajax({
          url: '/post_react/' + id,
          data: {
              'reaction': type
          },
          success: function (data) {
              $this.parent().siblings('.likes').text(data.like_count +   ' like');
              $this.parent().siblings('.dislikes').text(data.dislike_count + ' dislike');
              data.parent().siblings('.dislikes').style.textAlign = 'right';

              if (data.like_count === 0)
                  $this.parent().siblings('.likes').text('');



              if (data.dislike_count === 0)
                  $this.parent().siblings('.dislikes').text('');

          }
      });
    });



$('.reaction-comment').on('click', function () {
        alert('hi');
      var $this = $(this);
      var type = $this.attr('data-reaction');
      var id = $this.attr('data-id');
      $.ajax({
          url: '/comment_react/' + id,
          data: {
              'comment': type
          },
          success: function (data) {
              $this.parent().siblings('.comment').text(data.comment_count + '');

              if (data.comment_count === 0)
                  $this.parent().siblings('.comment').text('');
          }
      });
    });
});

