(function ($) {
  $(function () {


    $(".contact").click(function () {
      $("html, body").animate(
        { scrollTop: $(".contact--scroll").offset().top },
        1000
      );
    });

    $(".date").click(function () {
      $("html, body").animate(
        { scrollTop: $(".date--scroll").offset().top },
        1000
      );
    });

    $(".homework").click(function () {
      $("html, body").animate(
        { scrollTop: $(".homework--scroll").offset().top },
        1000
      );
    });
    $(".facebook").click(function () {
      $("html, body").animate(
        { scrollTop: $(".facebook--scroll").offset().top },
        1000
      );
    });
    $(".result").click(function () {
      $("html, body").animate(
        { scrollTop: $(".result--scroll").offset().top },
        1000
      );
    });

   

   


    

    
  });
})(jQuery);
