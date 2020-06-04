$(document).ready(function () {

    $('.add-to-cart-btn').click(function () {
        let product = $(this).parent().prev();
        let price_s = product.find('h4').text();
        let price_n = parseInt(price_s.split(' ')[0])
        let id = product.find('input').val();

        $.ajax({
            type: 'GET',
            url: '/goods/ajax_cart',
            data: 'test=15',
            success: function(result) {
                alert('AJAX work fine!');
            }
        });
    });

});