$(function () {

    $('.active').on('click', function () {
      var $this = $(this);
      var productId = $this.attr('data-id');
      $.ajax({
          url: '/boutique/activer/' + productId,
          data: {

          },
          success: function (data) {}


    })

     });
      });
