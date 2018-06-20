//Custom site js
$(document).ready(function(){
    //making footer fixed at the bottom if page content is not up to a screen
      //fxn to determine if an elt is visible on screen
      $.fn.isOnScreen = function(){

        var win = $(window);

        var viewport = {
            top : win.scrollTop(),
            left : win.scrollLeft()
        };
        viewport.right = viewport.left + win.width();
        viewport.bottom = viewport.top + win.height();

        var bounds = this.offset();
        bounds.right = bounds.left + this.outerWidth();
        bounds.bottom = bounds.top + this.outerHeight();

        return (!(viewport.right < bounds.left || viewport.left > bounds.right || viewport.bottom < bounds.top || viewport.top > bounds.bottom));

      };

      // Determine whether to make footer div fixed on load
      if($('#fixedMarker').isOnScreen()) {
          $(".footer").css({'position' : 'fixed', 'bottom' : '0px', 'left' : '0px', 'right' : '0px'});   //fix the left div
      }

});