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

  //Afiicher ou masquer un filtre sur la page boutique
  $('#filter-btn-motocyclette').click(function() {
      $('.content-table').hide();
      $('#boutique-moto-block').show();
      $('#filtre-moto').show();
      $('.filter-menu div').removeClass('active');
      $(this).addClass('active');
  });

  $('#filter-btn-accessoires').click(function() {
      $('.content-table').hide();
      $('#boutique-accessoires-block').show();
      $('#filtre-accessoires').show();
      $('.filter-menu div').removeClass('active');
      $(this).addClass('active');
  });

  $('#filter-btn-pieces').click(function() {
      $('.content-table').hide();
      $('#boutique-pieces-block').show();
      $('#filtre-pieces').show();
      $('.filter-menu div').removeClass('active');
      $(this).addClass('active');
  }); 

  //filtre pour les motos et les tricylce sur la page boutique
  $('#filtre-moto select').change(function() {
    // Récupérer les valeurs des champs du formulaire 
    var formData = $('#filtre-moto').serialize();
    console.log(formData);
    function formatPrice(price) {
      // Convertir le prix en chaîne de caractères
      let priceString = price.toString();
      // Utiliser une expression régulière pour ajouter un espace tous les 3 chiffres depuis la droite
      priceString = priceString.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
      return priceString;
    }
    // Envoyer une requête AJAX au serveur avec les données du formulaire
    $.ajax({ 
        url: '/filtre_moto/',
        data: formData,
        dataType: 'json',
        success: function(data) {
            // Mettre à jour la section des résultats avec les données reçues
            console.log("BOnjour le monde");
            console.log(data);
            $('.filter-search-button').text(`Résultats(${data.motos.length})`);
            var motosHTML = '';

        // Itérer à travers les données pour créer les éléments HTML correspondants
        data.motos.forEach(function(moto) {
            motosHTML += `
                <div class="col-6 col-md-3">
                    <div class="product_item">
                        <img class="" src="${moto.image}" alt="" width="100%">
                        <div class="bg-white p-2" style="border-radius: 0px 0px 5px 5px;">
                            <small>${moto.categorie}</small>
                            <div class="d-flex justify-content-between">
                                <h4 class="item_name">${moto.brand} ${moto.type_model}</h4>  
                                <p class="item_price">${formatPrice(moto.prix)} F</p> 
                            </div> 
                            <p>2019 &bullet; manuel &bullet; essence</p>
                            <div class="d-grid gap-1 pb-2"> 
                                <a class="btn btn_popular" href="/details/${moto.id}" type="button">Voir cette moto</a> 
                            </div>
                        </div> 
                    </div>
                </div>`;
        });

        // Mettre à jour la section des résultats avec les données reçues
        $('.resultats-moto').html(motosHTML);
        },
        error: function(xhr, status, error) {
            // Gérer les erreurs éventuelles
            console.error(xhr.responseText);
        }
    }); 
  }); 

  //Filtre pour les accessoires
  $('#filtre-accessoires').change(function() {
    // Récupérer les valeurs des champs du formulaire 
    var formData = $('#filtre-accessoires').serialize();
    console.log(formData);
    function formatPrice(price) {
      // Convertir le prix en chaîne de caractères
      let priceString = price.toString();
      // Utiliser une expression régulière pour ajouter un espace tous les 3 chiffres depuis la droite
      priceString = priceString.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
      return priceString;
    }
    // Envoyer une requête AJAX au serveur avec les données du formulaire
    $.ajax({ 
        url: '/filtre_accessoire/',
        data: formData,
        dataType: 'json',
        success: function(data) {
            // Mettre à jour la section des résultats avec les données reçues
            console.log("BOnjour le monde");
            console.log(data);
            $('#btn-search-accessoires').text(`Résultats(${data.accessoires.length})`);
            var accessoiresHTML = '';

        // Itérer à travers les données pour créer les éléments HTML correspondants
        data.accessoires.forEach(function(accessoire) {
            accessoiresHTML += `
                <div class="col-6 col-md-3">
                    <div class="product_item">
                        <img class="" src="${accessoire.image}" alt="" width="100%">
                        <div class="bg-white p-2" style="border-radius: 0px 0px 5px 5px;">
                            <small>${accessoire.categorie}</small>
                            <div class="d-flex justify-content-between">
                                <h4 class="item_name">${accessoire.name}</h4>  
                                <p class="item_price">${formatPrice(accessoire.prix)} F</p> 
                            </div>  
                            <div class="d-grid gap-1 pb-2"> 
                                <a class="btn btn_popular" href="/details/${accessoire.id}" type="button">Voir cet équipement</a> 
                            </div>
                        </div> 
                    </div>
                </div>`;
        });

        // Mettre à jour la section des résultats avec les données reçues
        $('.resultats-accessoires').html(accessoiresHTML);
        },
        error: function(xhr, status, error) {
            // Gérer les erreurs éventuelles
            console.error(xhr.responseText);
        }
    }); 
  }); 

  //Filtre pour les pieces
  $('#filtre-pieces').change(function() {
    // Récupérer les valeurs des champs du formulaire 
    var formData = $('#filtre-pieces').serialize();
    console.log(formData);
    function formatPrice(price) {
      // Convertir le prix en chaîne de caractères
      let priceString = price.toString();
      // Utiliser une expression régulière pour ajouter un espace tous les 3 chiffres depuis la droite
      priceString = priceString.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
      return priceString;
    }
    // Envoyer une requête AJAX au serveur avec les données du formulaire
    $.ajax({ 
        url: '/filtre_piece/',
        data: formData,
        dataType: 'json',
        success: function(data) {
            // Mettre à jour la section des résultats avec les données reçues
            console.log("BOnjour le pièces");
            console.log(data);
            $('#btn-search-pieces').text(`Résultats(${data.pieces.length})`);
            var piecesHTML = '';

        // Itérer à travers les données pour créer les éléments HTML correspondants
        data.pieces.forEach(function(piece) {
            piecesHTML += `
                <div class="col-6 col-md-3">
                    <div class="product_item">
                        <img class="" src="${piece.image}" alt="" width="100%">
                        <div class="bg-white p-2" style="border-radius: 0px 0px 5px 5px;">
                            <small>${piece.categorie}</small>
                            <div class="d-flex justify-content-between">
                                <h4 class="item_name">${piece.name}</h4>  
                                <p class="item_price">${formatPrice(piece.prix)} F</p> 
                            </div>  
                            <div class="d-grid gap-1 pb-2"> 
                                <a class="btn btn_popular" href="/details/${piece.id}" type="button">Voir cet équipement</a> 
                            </div>
                        </div> 
                    </div>
                </div>`;
        });

        // Mettre à jour la section des résultats avec les données reçues
        $('.resultats-pieces').html(piecesHTML);
        },
        error: function(xhr, status, error) {
            // Gérer les erreurs éventuelles
            console.error(xhr.responseText);
        }
    }); 
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

