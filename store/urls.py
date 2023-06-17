from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'), 
    path('navigation/', views.navigation, name='navigation'),
    path('checkout/', views.checkout, name='checkout'),
    path('boutique/', views.boutique, name='boutique'),
    path('details/<int:moto_id>', views.details, name='details'),
    path('categories/<slug:categorie_slug>', views.detail_categorie, name='categorie')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)