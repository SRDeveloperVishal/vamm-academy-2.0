
  $(document).ready(function() {
 
    $("#owl-demo").owlCarousel({
   
        navigation : true, // Show next and prev buttons
   
        slideSpeed : 300,
        paginationSpeed : 400,
   
        items : 1, 
        itemsDesktop : true,
        itemsDesktopSmall : true,
        itemsTablet: true,
        itemsMobile : true,
        autoplay:true,
        smartSpeed:50,
        loop:true
   
    });
   
  });