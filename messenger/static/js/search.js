$(function () {
  function debounce(callback, duration) {
    var timer;
    return function () {
      clearTimeout(timer);
      timer = setTimeout(callback, duration);
    }
  }

  var $pager = $('.pager')
  function search(page) {
    $.ajax({
      url: '/messages/filter/',
      type: 'GET',
      data: {
        q: $('#product-search').val(),
        page: page

      },
      cache: false,
      success: function (data) {
        console.log(data);
        $('.produit').hide().html(data).fadeIn('slow');
        page = $(".page").val();
        $pager.attr('data-current-page', page);

      }
    });
  }

  $('#product-search').on('keyup', debounce(function () {
    search();
  }, 500));
  $('#next').on('click', function () {
    var page = parseInt($pager.attr('data-current-page'));
    search(page+1);
  });
  $('#prev').on('click', function () {
    var page = parseInt($pager.attr('data-current-page'));
    search(page-1);
  });
});