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



<!-- Script below adapted from https://elementorcodes.com/elementor-header-show-scroll-up/ -->

  document.addEventListener('DOMContentLoaded', function() {
  jQuery(function($){
  var mywindow = $(window);
  var mypos = mywindow.scrollTop();
  mywindow.scroll(function() {
  if (mypos > 120) {
  if(mywindow.scrollTop() > mypos) {
  $('#stickyheaders').addClass('headerup');
  } else {
  $('#stickyheaders').removeClass('headerup');
  }
  }
  mypos = mywindow.scrollTop();
  }); }); });
  