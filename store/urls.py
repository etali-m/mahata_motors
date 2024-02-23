from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('panier-moto/', views.panier_moto, name='panier_moto'),  
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name="update_item"),
    path('boutique/', views.boutique, name='boutique'),
    path('get_modeles/', views.get_modeles, name='get_modeles'),
    path('get_annees/', views.get_annees, name='get_annees'),
    path('filtre_moto/', views.filtre_moto, name="filtre_moto"),
    path('filtre_accessoire/', views.filtre_accessoire, name='filtre_accessoire'),
    path('filtre_piece/', views.filtre_piece, name='filtre_piece'),
    path('get_colors/', views.get_colors, name='get_colors'),

    path('details/<int:moto_id>', views.details, name='details'),
    path('details_2/<int:item_id>', views.details_item, name='details-item'),

    path('categories/<slug:categorie_slug>', views.detail_categorie, name='categorie'),

    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('paiement-method/', views.paiment_method, name='paiement-method'),
    path('sav/', views.sav, name='sav'),
    path('sav/<int:num_chassis>', views.suivie_sav, name='suivie-sav'),
    path('how-to-buy/', views.how_to_buy, name='how-to-buy'),
    path('devenir-vendeur/', views.vendeur, name='vendeur'),
    path('devenir-assembleur/', views.assembleur, name='assembleur'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)