$(function () {
    $('.collections').on('click', '.delete-collection', function (e) {
        e.preventDefault();
        var $this = $(this);
        var collectionId = $this.attr('data-collection-id');
        
        if (confirm('Are you sure?'))
            $.ajax({
                url: '/wishlist/collection/' + collectionId + '/delete',
                type: 'POST',
                success: function (data) {
                    if (data.success)
                        $this.closest('.col-md-4').fadeOut().remove();
                }
            });
    });
    $('.new-collection').on('click', function (e) {
        e.preventDefault();
        $('.new-collection-container').slideToggle();
        $('.new-collection-input').focus();
    });
    $('.new-collection-form').on('submit', function (e) {
        e.preventDefault();
        var $this = $(this);
        var collectionName = $('.new-collection-input').val();
        if (collectionName.trim().length > 0) 
            $.ajax({
                url: '/wishlist/collection/new',
                type: 'POST',
                data: {
                    name: collectionName,
                },
                success: function (data) {
                    if (data.success) {
                        $('.new-collection-container').slideToggle();
                        $('.new-collection-input').val('');
                        $('.collections').prepend('<div class="col-md-4">' + data.collection + "</div>");
                    }
                }
            });
    });
    $('.collection-items').on('click', '.remove-product', function (e) {
        e.preventDefault();
        if (confirm('Are you sure?')) {
            var $this = $(this);
            var productId = $this.attr('data-product-id');
            var collectionId = $this.attr('data-collection-id');
            $.ajax({
                url: '/wishlist/collection/' + collectionId + '/remove/' + productId,
                type: 'POST',
                success: function (data) {
                    if (data.success) {
                        $this.closest('.collection-item').fadeOut().remove();
                        if (data.count > 0)
                            $('#item-count').text("(" + data.count + "items)")
                        else
                            $('#item-count').text("");
                    }
                }
            });
        }
    });
});