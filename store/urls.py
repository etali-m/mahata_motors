from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('boutique/', views.boutique, name='boutique'),
]