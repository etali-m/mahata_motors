/* responsive menu */
$(document).ready(function(){
  $('.navigation_responsive').hide();
  $('.navigation_responsive_sub').hide();

  //afficher les sous menu du menu responsive au click
  $('.navigation_responsive_menu').click(function(){
    $(this).find('.responsive__chevron').toggleClass('fa-chevron-down fa-chevron-up');
    $(this).next('.navigation_responsive_sub').slideToggle();
  });

  //afficher ou masquer le menu au click sur le bouton
  $('.menu-btn').click(function(){
    $('.navigation_responsive').slideToggle();
  });
  
});

var swiper1 = new Swiper('#swiper1', {

    breakpoints: {
      768:{
        slidesPerView: 3,
        spaceBetween: 10,
      },
      425:{
        slidesPerView: 2,
        spaceBetween: 20,
      },
      320:{
        slidesPerView: 1,
        spaceBetween: 30,
      }
    },
    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper .swiper-button-next',
      prevEl: '.swiper .swiper-button-prev',
    }, 
});
 
var swiper2 = new Swiper ('#swiper2', {
  breakpoints: {
    768:{
      slidesPerView: 4,
      spaceBetween: 10,
    },
    425:{
      slidesPerView: 3,
      spaceBetween: 20,
    },
    320:{
      slidesPerView: 2,
      spaceBetween: 30,
    }
  },
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  autoplay: {
      delay: 2500, 
  },
});

/* slider de photo de la page de details */
var swiper3 = new Swiper('#swiper3', {

  breakpoints: {
    768:{
      slidesPerView: 3,
      spaceBetween: 10,
    },
    425:{
      slidesPerView: 2,
      spaceBetween: 20,
    },
    320:{
      slidesPerView: 1,
      spaceBetween: 30,
    }
  },
  // Optional parameters
  direction: 'horizontal',
  loop: true,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper .swiper-button-next',
    prevEl: '.swiper .swiper-button-prev',
  }, 
});


/* slider de photo de la page de details accessoire et pièces */
var swiper4 = new Swiper('#swiper4', {

  breakpoints: {
    768:{
      slidesPerView: 1,
      spaceBetween: 10,
    },
    425:{
      slidesPerView: 1,
      spaceBetween: 20,
    },
    320:{
      slidesPerView: 1,
      spaceBetween: 30,
    }
  },
  // Optional parameters
  direction: 'horizontal',
  loop: true,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper .swiper-button-next',
    prevEl: '.swiper .swiper-button-prev',
  }, 
});


/* slider de photo de la page de details */



const menuBtn = document.querySelector('.menu-btn');
	let menuOpen = false;

	menuBtn.addEventListener('click', () =>{
		if(!menuOpen){
			menuBtn.classList.add('open');
			menuOpen = true;
		} else {
			menuBtn.classList.remove('open');
			menuOpen = false;
		}
});

// loader
/*window.addEventListener("load", function() {
  document.getElementById("loader").style.display = "none";
});*/

