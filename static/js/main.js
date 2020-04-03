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
$('.filter li .filteroption').on("click", function() {
    var value = $(this).attr('data-name');
    $grid.isotope({
        filter: value
    });
    $('.filter li .filteroption').removeClass('active');
    $(this).addClass('active');
});


$('.sort li a').on("click", function() {
    var value = $(this).attr('data-name');
    $grid.isotope({
        sortBy: value
    });
    $('.sort li a').removeClass('active');
    $(this).addClass('active');
})


// Toggle Hamburger when close / open modal
var $hamburger = $(".hamburger--spring, .modal-close");
$hamburger.on("click", function(e) {
    $hamburger.toggleClass("is-active");
    
});