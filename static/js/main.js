// ** USE ISOTOPE FRAMEWORK FOR FILTERING AND SORTING **


$(document).ready(function() {

    // ----------- * FILTERING * -----------

    jQuery(function() {
        console.log("Filtering started");

        // BUG: The filtering happens before the images are loaded, so the grid breaks.
        // Try to fix by waiting for images to load
        // Same issue discussed here: https://github.com/metafizzy/isotope/issues/611

        // var $container = jQuery('.grid-main');
        // $container.imagesLoaded(function() {
        $grid.isotope({
            filter: '*',
            layoutMode: 'fitRows'
        });
        // });
        console.log("Filtering done");
    });

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
            cookingtime: '.cookingtime parseInt',
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




/* Toggle Hamburger when close / open modal
var $hamburger = $(".hamburger--spring, .modal-close");
$hamburger.on("click", function(e) {
    $hamburger.toggleClass("is-active");
    
});
*/

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