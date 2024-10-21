let questions = document.querySelectorAll(".faq__question");
questions.forEach((question) => {
    question.addEventListener("click", function () {
        question.classList.toggle("faq__question_active");
        const nextElement = question.nextElementSibling;
        nextElement.classList.toggle("faq__panel_active");
    });
});

document.addEventListener("DOMContentLoaded", function () {

    var sidebarLinks = document.querySelectorAll('#sidebar a li');

    sidebarLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        var activeLink = document.querySelector('#sidebar a li.active');
        if (activeLink) {
          activeLink.classList.remove('active');
        }
        this.classList.add('active');
      });
    });
    // ----------------------

    $('.main-content .owl-carousel').owlCarousel({
        autoplay: true,
        autoplayTimeout: 4000,
        stagePadding: 30,
        loop: true,
        margin: 10,
        nav: true,
        navText: [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        navContainer: '.main-content .custom-nav',
        responsive: {
            0:{
             items:1
            },
            410: {
                items: 2
            },
            600: {
                items: 2
            },
            991: {
                items: 3
            },
            1200: {
                items: 4
            },
            1400: {
                items: 6
            }
    }
});

    $('.index-gallery').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        navText: [
            "<i class='fa fa-caret-left'></i>",
            "<i class='fa fa-caret-right'></i>"
        ],
        autoplay: true,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items:1
            }
        }
    })

    

    $(document).ready(function () {
        $('#search-icn').click(function () {
            $('.dearch-div').slideToggle("slow");
            // Alternative animation for example
            // slideToggle("fast");
        });
    });
});





    