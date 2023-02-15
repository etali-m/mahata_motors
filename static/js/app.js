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

/* responsive menu */
