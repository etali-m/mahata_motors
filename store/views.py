from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required 
 
from urllib.parse import urlencode, unquote
from random import shuffle

from .models import *
 

def home(request):
    #motos = list(MotorBike.objects.all()) + list(Tricycle.objects.all())
    motos = Moto.objects.all() 
    brands = Brand.objects.all()[:12]
    context = {'motos':motos, 'brands':brands } 
    return render(request, 'store/home.html', context)

 

def boutique(request): 

    #on recupére les éléments du entrés dans le champs de recherche
    query = request.GET.get('query') 
    #On recupère les options de sélection des filtres soumises par l'utilisateur
    marque = request.GET.get('marque')
    type = request.GET.get('type')
    gamme = request.GET.get('gamme')
    prix_max = request.GET.get('prix')

    #on récupère les éléments pour le menu de navigation 
    #commercials = MotorBike.objects.all()[:8]

    #on recupère toutes les marques pour les filtres 
    #sauf les marques bazar, cocimecam, senke
    brands = Brand.objects.all().exclude(name__icontains='Bazar').exclude(name__icontains='cocimecam').exclude(name__icontains='senke')
 

    motos = Moto.objects.all() 
    equipements = Equipement.objects.all() 

    """
   if query and query!="":
        motos = MotorBike.objects.filter(Q(name__icontains=query) | Q(brand__name__icontains=query))
        tricycles = Tricycle.objects.filter(name__icontains=query)
        accessoires = Accessory.objects.filter(name__icontains=query)

 
   
   #si il y a des filtres qui sont choisis
    if marque:
        motos = motos.filter(brand__name__icontains=marque)
        tricycles = tricycles.filter(brand__name__icontains=marque)
        accessoires = accessoires.filter(name__icontains=marque)
    if type:
        motos = motos.filter(categorie__name__icontains=type)
        tricycles = tricycles.filter(categorie__name__icontains=type)
        accessoires = accessoires.filter(Q(categorie__name__icontains=type) | Q(categorie__parent_category__name__icontains=type))
    if gamme:
        motos = motos.filter(usage__icontains=gamme)
    if prix_max:
        motos = motos.filter(price__lte=prix_max)
    """
    context = {
                'motos': motos,
                'equipements': equipements, 
               }

    return render(request, 'store/boutique.html', context)
 

def details(request, moto_id):
    #on verifie si l'objet est une  

    moto = get_object_or_404(Moto, id=moto_id)  
    #moto_images = moto.images.all()
    similars = Moto.objects.filter(categorie= moto.categorie).exclude(id=moto.id)[:5] 
    
    
    
    context = {'moto':moto, 
               #'moto_images': moto_images,
               'similars':similars }

        
    return render(request, 'store/details.html', context)


def details_item(request, item_id):
    #on verifie si l'objet est une 
    #les catégories pour le menu de navigation 
 
    item = get_object_or_404(Equipement, id=item_id) 
    item_images = Images.objects.filter(product=item)
    similars = Equipement.objects.filter(categorie= item.categorie).exclude(id=item.id)[:5]
     
    
    
    
    context = {'item':item, 
               'item_images': item_images,
               'similars':similars 
               }

        
    return render(request, 'store/details_2.html', context)



def detail_categorie(request, categorie_slug): 
    #On recupère toutes les categories pour le menu
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')
    brands = Brand.objects.all()[:5]

    #on recupère les élément de la categorie
    category = get_object_or_404(Categorie, slug=categorie_slug.lower())
    subcategories = Categorie.objects.filter(parent_category=category) 
    target_categories = ["Motocyclette", "Tricycle"]

    products = []

    # Iterate through subcategories and collect products
    for subcategory in subcategories:
        if subcategory.name in ["Motocyclette", "Tricycle"]:
            # If the subcategory is a motorcycle or tricycle, retrieve products of the Moto model
            products.extend(Moto.objects.filter(categorie=subcategory))
        else:
            # Otherwise, retrieve products of the Equipement model
            products.extend(Equipement.objects.filter(categorie=subcategory))

    # If no subcategories exist, retrieve products directly from the selected category
    if not subcategories:
        if category.name in ["Motocyclette", "Tricycle"]:
            # If the selected category is a motorcycle or tricycle, retrieve products of the Moto model
            products.extend(Moto.objects.filter(categorie=category))
        else:
            # Otherwise, retrieve products of the Equipement model
            products.extend(Equipement.objects.filter(categorie=category))

    print(products)

    # Shuffle the list of products
    shuffle(products)
    
    
    
    context = {
        'categories':categories,
        'categorie':category,  
        'products':products,
        'subcategories':subcategories,
        'brands':brands,
        'target_categories': target_categories
    }
    return render(request,'store/categorie.html', context)



def cart(request):
    #les catégories pour le menu de navigation
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'categories': categories, 'items':items, 'order':order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order, 'categories':categories}
    return render(request, 'store/checkout.html', context)


def contact(request):
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')

    context={
        'categories':categories,
    }

    return render(request, 'store/contact.html', context)


def about(request):
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')

    context={
        'categories':categories,
    }

    return render(request, 'store/a-propos.html', context)


def services(request):
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')

    context={
        'categories':categories,
    }

    return render(request, 'store/services.html', context)


def paiment_method(request):
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')

    context={
        'categories':categories,
    }

    return render(request, 'store/paiement-method.html', context)


def sav(request): 

    context={ 
    }

    return render(request, 'store/sav.html', context)

def suivie_sav(request, num_chassis):
    context={ }

    return render(request, 'store/suivie-sav.html', context)    


def how_to_buy(request):
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')

    context={
        'categories':categories,
    }

    return render(request, 'store/how-to-buy.html', context)


def assembleur(request):
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')

    context={
        'categories':categories,
    }

    return render(request, 'store/technicien-assembleur.html', context)


def vendeur(request):
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')

    context={
        'categories':categories,
    }

    return render(request, 'store/vendeur.html', context)