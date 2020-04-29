// ** USE ISOTOPE FRAMEWORK FOR FILTERING AND SORTING **


// Use window load function to ensure all images are loaded before isotope loads
// Otherwise the grid will break
$(window).on("load", function() {

    // ----------- * FILTERING * -----------

    // Filter by category 
    $('.filter li .filteroption').on("click", function() {
        var value = $(this).attr('data-name');
        $grid.isotope({
            filter: value,
            layoutMode: 'fitRows'
        });
        // Remove active class from all
        $('.filter li .filteroption').removeClass('active');
        // Add active class to 'this'
        $(this).addClass('active');
    });


    // ----------- * SORTING * -----------
    // Get sort data

    var $grid = $('.grid-main').isotope({
        itemSelector: '.grid-item',
        layoutMode: 'fitRows',
        getSortData: {
            name: function(element) {
                return $(element).text();
            },
            // Sort by cooking time?
            //cookingtime: '.cookingtime parseInt',
        }
    });


    // Sort by name, original or random 
    $('.sort li a').on("click", function() {
        var value = $(this).attr('data-name');
        $grid.isotope({
            sortBy: value
        });
        // Remove active class from all
        $('.sort li a').removeClass('active');
        // Add active class to this
        $(this).addClass('active');
    });




});



// ----------- * HEADER * -----------

// Script below adapted from https://elementorcodes.com/elementor-header-show-scroll-up/
// Remove sticky header on scroll down and reveals on scroll up (from any page location)
document.addEventListener('DOMContentLoaded', function() {
    jQuery(function($) {
        var mywindow = $(window);
        var mypos = mywindow.scrollTop();
        mywindow.scroll(function() {
            if (mypos > 120) {
                if (mywindow.scrollTop() > mypos) {
                    $('#stickyheaders').addClass('headerup');
                } else {
                    $('#stickyheaders').removeClass('headerup');
                }
            }
            mypos = mywindow.scrollTop();
        });
    });
});
// End of adapted snippet from https://elementorcodes.com/elementor-header-show-scroll-up/


// ----------- * HIDE & SHOW * -----------

// Show and hide featured images in recipe.html  when associated button is hovered //
$(document).ready(function() {

    $('.featured-utensil-button-2').hover(function() {
        $('.featured-utensil-image-1').addClass('display-2');
        $('.featured-utensil-image-1').removeClass('display-1');
        $('.featured-utensil-image-2').removeClass('display-2');
        $('.featured-utensil-image-2').addClass('display-1');
    }, function() {
        $('.featured-utensil-image-2').addClass('display-2');
        $('.featured-utensil-image-2').removeClass('display-1');
        $('.featured-utensil-image-1').addClass('display-1');
        $('.featured-utensil-image-1').removeClass('display-2');
    });

    $('.featured-utensil-button-3').hover(function() {
        $('.featured-utensil-image-1').addClass('display-2');
        $('.featured-utensil-image-1').removeClass('display-1');
        $('.featured-utensil-image-3').removeClass('display-3');
        $('.featured-utensil-image-3').addClass('display-1');
    }, function() {
        $('.featured-utensil-image-3').addClass('display-3');
        $('.featured-utensil-image-3').removeClass('display-1');
        $('.featured-utensil-image-1').addClass('display-1');
        $('.featured-utensil-image-1').removeClass('display-2');
    });


});