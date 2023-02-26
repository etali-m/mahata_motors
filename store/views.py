from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
def home(request):
    motos = list(MotorBike.objects.all()) + list(Tricycle.objects.all())
    brands = Brand.objects.all()[:12]
    context = {'motos':motos, 'brands':brands} 
    return render(request, 'store/home.html', context)


def moto(request):
    motos = list(MotorBike.objects.all()) + list(Tricycle.objects.all())
    context = {'motos':motos}
    return render(request, 'store/motos.html', context)


def details(request, moto_id):
    #on verifie si l'objet est une moto
    try:
        moto = get_object_or_404(MotorBike, id=moto_id) 
        similars = MotorBike.objects.filter(genre= moto.genre).exclude(id=moto.id)[:5]
    #Si l'objet n'est pas une moto on verifie qu'il est un tricycle
    except Http404:
        moto = get_object_or_404(Tricycle, id=moto_id)
        similars = Tricycle.objects.filter(genre= moto.genre).exclude(id=moto.id)[:5]
    
    
    
    context = {'moto':moto, 'similars':similars}

        
    return render(request, 'store/details.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)