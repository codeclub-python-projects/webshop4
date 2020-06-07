$(document).ready(function () {

    $('.add-to-cart-btn').click(function () {
        let product = $(this).parent().prev();
        let price_s = product.find('h4').text();
        let price_n = parseInt(price_s.split(' ')[0])
        let id = product.find('input').val();

        $.ajax({
			type: 'GET',
			url: 'catalog',
			data: `pid=${id}&price=${price_n}`,
			success: function(result) {
				alert('AJAX-OK');
				alert(result.test);
				alert(result.count);
				alert(result.amount);
			}
		});
    });

});