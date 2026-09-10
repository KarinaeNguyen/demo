/******************************************
    Version: 1.0
/****************************************** */

(function ($) {
    "use strict";

    /* ==============================================
     Fixed menu & Smart Mobile Scroll-Up Reveal
     =============================================== */

    var lastScrollTop = 0;
    var deltaScroll = 5;

    $(window).on('scroll', function () {
        var currentScrollTop = $(this).scrollTop();

        // Standard fixed-menu toggle
        if (currentScrollTop > 50) {
            $('.header_style_01').addClass('fixed-menu');
        } else {
            $('.header_style_01').removeClass('fixed-menu');
        }

        // Mobile Smart Hide on Scroll Down, Reveal on Scroll Up
        if ($(window).width() < 992) {
            // Check if scroll difference exceeds threshold
            if (Math.abs(lastScrollTop - currentScrollTop) > deltaScroll) {
                if (currentScrollTop > lastScrollTop && currentScrollTop > 70) {
                    // Scrolling DOWN: slide up and hide header if mobile menu is not expanded
                    if (!$('#navbar').hasClass('in')) {
                        $('.header_style_01').addClass('header-scroll-hidden');
                    }
                } else if (currentScrollTop < lastScrollTop) {
                    // Scrolling UP: slide down and reveal header
                    $('.header_style_01').removeClass('header-scroll-hidden');
                }
            }

            // Always show at the top of the page
            if (currentScrollTop <= 50) {
                $('.header_style_01').removeClass('header-scroll-hidden');
            }
        } else {
            $('.header_style_01').removeClass('header-scroll-hidden');
        }

        lastScrollTop = currentScrollTop <= 0 ? 0 : currentScrollTop;
    });

    // Ensure header is fully visible when mobile toggle is tapped
    $('.navbar-toggle').on('click', function () {
        $('.header_style_01').removeClass('header-scroll-hidden');
    });


    /* ==============================================
         Scroll to top  
     ============================================== */

    if ($('#scroll-to-top').length) {
        var scrollTrigger = 100, // px
            backToTop = function () {
                var scrollTop = $(window).scrollTop();
                if (scrollTop > scrollTrigger) {
                    $('#scroll-to-top').addClass('show');
                } else {
                    $('#scroll-to-top').removeClass('show');
                }
            };
        backToTop();
        $(window).on('scroll', function () {
            backToTop();
        });
        $('#scroll-to-top').on('click', function (e) {
            e.preventDefault();
            $('html,body').animate({
                scrollTop: 0
            }, 700);
        });
    }

    /* ==============================================
       LOADER (Enforce 1.5s minimum display duration) -->
        =============================================== */

    var preloaderStartTime = Date.now();
    var minPreloaderDuration = 1500; // 1.5 seconds minimum display duration

    function removePreloader() {
        var $pre = $("#preloader, .preloader");
        if ($pre.length && !$pre.hasClass("loaded")) {
            $pre.addClass("loaded").fadeOut(400, function () {
                $(this).css({
                    "display": "none",
                    "visibility": "hidden",
                    "pointer-events": "none",
                    "opacity": "0"
                });
            });
        }
    }

    $(window).on('load', function () {
        var elapsed = Date.now() - preloaderStartTime;
        var remainingTime = Math.max(0, minPreloaderDuration - elapsed);
        setTimeout(removePreloader, remainingTime);
    });

    // Fallback: guaranteed to close after 4 seconds even if external assets or network stall
    setTimeout(removePreloader, 4000);

    /* ==============================================
     FUN FACTS -->
     =============================================== */

    function count($this) {
        var current = parseInt($this.html(), 10);
        current = current + 50; /* Where 50 is increment */
        $this.html(++current);
        if (current > $this.data('count')) {
            $this.html($this.data('count'));
        } else {
            setTimeout(function () {
                count($this)
            }, 30);
        }
    }
    $(".stat_count, .stat_count_download").each(function () {
        $(this).data('count', parseInt($(this).html(), 10));
        $(this).html('0');
        count($(this));
    });


	/* ==============================================
     FUN FACTS -->
     =============================================== */

    $(".slider-wrapper").owlCarousel({
        items: 1,
        nav: true,
        dots: false,
        autoplay: true,
        loop: true,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        mouseDrag: false,
        touchDrag: false,
        smartSpeed: 700
    });





    /* ==============================================
     TOOLTIP -->
     =============================================== */
    $('[data-toggle="tooltip"]').tooltip()
    $('[data-toggle="popover"]').popover()

    /* ==============================================
     CONTACT -->
     =============================================== */
    jQuery(document).ready(function () {
        $('#contactform').submit(function () {
            var action = $(this).attr('action');
            $("#message").slideUp(750, function () {
                $('#message').hide();
                $('#submit')
                    .after('<img src="images/ajax-loader.gif" class="loader" />')
                    .attr('disabled', 'disabled');
                $.post(action, {
                    first_name: $('#first_name').val(),
                    last_name: $('#last_name').val(),
                    email: $('#email').val(),
                    phone: $('#phone').val(),
                    select_service: $('#select_service').val(),
                    select_price: $('#select_price').val(),
                    comments: $('#comments').val(),
                    verify: $('#verify').val()
                },
                    function (data) {
                        document.getElementById('message').innerHTML = data;
                        $('#message').slideDown('slow');
                        $('#contactform img.loader').fadeOut('slow', function () {
                            $(this).remove()
                        });
                        $('#submit').removeAttr('disabled');
                        if (data.match('success') != null) $('#contactform').slideUp('slow');
                    }
                );
            });
            return false;
        });
    });

    /* ==============================================
     CODE WRAPPER -->
     =============================================== */

    $('.code-wrapper').on("mousemove", function (e) {
        var offsets = $(this).offset();
        var fullWidth = $(this).width();
        var mouseX = e.pageX - offsets.left;

        if (mouseX < 0) {
            mouseX = 0;
        } else if (mouseX > fullWidth) {
            mouseX = fullWidth
        }

        $(this).parent().find('.divider-bar').css({
            left: mouseX,
            transition: 'none'
        });
        $(this).find('.design-wrapper').css({
            transform: 'translateX(' + (mouseX) + 'px)',
            transition: 'none'
        });
        $(this).find('.design-image').css({
            transform: 'translateX(' + (-1 * mouseX) + 'px)',
            transition: 'none'
        });
    });
    $('.divider-wrapper').on("mouseleave", function () {
        $(this).parent().find('.divider-bar').css({
            left: '50%',
            transition: 'all .3s'
        });
        $(this).find('.design-wrapper').css({
            transform: 'translateX(50%)',
            transition: 'all .3s'
        });
        $(this).find('.design-image').css({
            transform: 'translateX(-50%)',
            transition: 'all .3s'
        });
    });

    /* ==============================================
       Subtle Scroll Reveal & Rolling Counter for Statistics Section
       ============================================== */
    var statsAnimated = false;

    function triggerStatsAnimation() {
        if (statsAnimated) return;
        var $statSection = $('#statistics');
        if (!$statSection.length) return;

        statsAnimated = true;
        $statSection.addClass('qp-stats-visible');

        // Delay number roll slightly so the card reveal motion is already underway
        setTimeout(function () {
            $('.counter').each(function (idx) {
                var $this = $(this);
                var target = parseInt($this.attr('data-count'), 10);
                if (isNaN(target)) return;

                $({ countNum: 0 }).delay(idx * 70).animate({ countNum: target }, {
                    duration: 2000,
                    easing: 'swing',
                    step: function () {
                        var val = Math.floor(this.countNum);
                        if (target >= 1000) {
                            $this.text(val.toLocaleString('vi-VN'));
                        } else {
                            $this.text(val);
                        }
                    },
                    complete: function () {
                        if (target >= 1000) {
                            $this.text(target.toLocaleString('vi-VN'));
                        } else {
                            $this.text(target);
                        }
                    }
                });
            });
        }, 280);
    }

    var $statSection = $('#statistics');
    if ($statSection.length) {
        // Initialize counter display to 0
        $('.counter').text('0');

        if ('IntersectionObserver' in window) {
            var statsObserver = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting && !statsAnimated) {
                        triggerStatsAnimation();
                        statsObserver.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.15,
                rootMargin: '0px 0px -40px 0px'
            });
            statsObserver.observe($statSection[0]);
        } else {
            // Robust fallback for older browsers
            function checkStatsScroll() {
                if (statsAnimated) return;
                var rect = $statSection[0].getBoundingClientRect();
                var vh = window.innerHeight || document.documentElement.clientHeight;
                if (rect.top <= vh * 0.85 && rect.bottom >= 0) {
                    triggerStatsAnimation();
                    $(window).off('scroll resize', checkStatsScroll);
                }
            }
            $(window).on('scroll resize', checkStatsScroll);
            $(document).ready(checkStatsScroll);
        }
    }

})(jQuery);