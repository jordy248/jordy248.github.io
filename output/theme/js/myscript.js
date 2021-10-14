jQuery(window).on("load", function() {
    jQuery('body').removeClass('loading');
});

jQuery('#show-disqus').on('click', function() {
    jQuery(this).parent().addClass('activated');
});

jQuery('.experience').on('click', function() {
    jQuery(this).toggleClass('active');
});