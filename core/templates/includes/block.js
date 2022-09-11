


<a href="#" class="back-to-top"><i class="fa fa-angle-up"></i></a>

<script src="static/js/jquery-3.6.1.min.js"></script>
<script src="static/js/bootstrap.bundle.js"></script>
<script src="static/owlcarousel/js/owl.carousel.min.js"></script>
<script src="static/js/script.js"></script>
<script>
    var owl = $('.owl-carousel');
    owl.owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: false,
        autoplay: true,
        autoplayTimeout: 2e3,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            400: {
                items: 2
            },
            700: {
                items: 3
            },
            1000: {
                items: 5
            }
        }
    });
</script>