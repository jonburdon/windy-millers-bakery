var $grid = $('.grid-main').isotope({
    itemSelector: '.grid-item',
    layoutMode: 'fitRows',
    getSortData: {
        name: function(element) {
            return $(element).text();
        },
        cookingtime: '.cookingtime parseInt',
    }
});
$('.filter button').on("click", function() {
    var value = $(this).attr('data-name');
    $grid.isotope({
        filter: value
    });
    $('.filter button').removeClass('active');
    $(this).addClass('active');
});
$('.sort button').on("click", function() {
    var value = $(this).attr('data-name');
    $grid.isotope({
        sortBy: value
    });
    $('.sort button').removeClass('active');
    $(this).addClass('active');
})