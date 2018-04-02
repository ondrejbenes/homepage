$("a.nav-link").on("click", function(){
    $("a.nav-link.active").removeClass("active");
    $(this).addClass("active");
    $('html, body').animate({
        scrollTop: $($(this).attr('href')).offset().top - 60
    }, 500);
});