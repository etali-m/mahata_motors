from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
import json
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


#cette fonction est utilisé pour recupére le modèle de motos pour ajax
def get_modeles(request):
    marque = request.GET.get('marque')
    print(marque)
    if marque :
        modeles = Moto.objects.filter(brand__name__icontains=marque).values_list('type_model', flat=True).distinct()
        modele_dict = {str(i): modele for i, modele in enumerate(modeles)} 
        return JsonResponse({'modeles': modele_dict})
    else:
        return JsonResponse({'modeles':{}})

#Cette fonction est utilisé par ajax sur la page boutique pour récupérer les années correspondante à un modele de moto
def get_annees(request):
    modele = request.GET.get('modele')
    print(modele)
    if modele:
        #on récupère les années des motos on effectue un filtre sur les motos et des ces motos on récupère uniquement le champs année grace à la fonction value_list()
        annees = Moto.objects.filter(type_model=modele).values_list('annee', flat=True) 
        annee_dict = {str(i): annee for i, annee in enumerate(annees)}
        return JsonResponse({'annees': annee_dict})
    else:
        return JsonResponse({'annees': {}})



def get_colors(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        size = request.GET.get('size')

        try:
            product = Product.objects.get(id=product_id)
            variations = ProductVariation.objects.filter(product=product, size=size)

            data = []
            for variation in variations:
                data.append({
                    'id': variation.id, 
                    'image': variation.color_image.url,
                })
            print(data)
            return JsonResponse(data, safe=False)

        except Product.DoesNotExist:
            return JsonResponse({'error': 'Produit non trouvé'}, status=404)

    return JsonResponse({'error': 'Requête non autorisée'}, status=403)

def boutique(request): 

    #on recupére les éléments du entrés dans le champs de recherche
    query = request.GET.get('query') 
    #On recupère les options de sélection des filtres soumises par l'utilisateur
    marque = request.GET.get('marque')
    marque_piece = request.GET.get('marque_piece')
    type = request.GET.get('type')
    gamme = request.GET.get('gamme')
    prix_max = request.GET.get('prix')
    year = request.GET.get('year')
    modele = request.GET.get('modele')


    type_accessoire = request.GET.get('accessoire')


    #on recupère toutes les marques pour les filtres 
    #sauf les marques bazar, cocimecam, senke
    brands = Brand.objects.all().exclude(name__icontains='Bazar').exclude(name__icontains='cocimecam').exclude(name__icontains='senke')
    type_accessoires = Categorie.objects.filter(parent_category__name__icontains='accéssoires')
    
    print(type_accessoires)

    motos = Moto.objects.all() 
    accessoires = Equipement.objects.filter(Q(categorie__name__icontains='accéssoires') | Q(categorie__parent_category__name__icontains='accéssoires'))
    pieces = Equipement.objects.filter(Q(categorie__name__icontains='pièce') | Q(categorie__parent_category__name__icontains='pièce'))
 

    if query and query!="":
        accessoires = []
        pieces = []
        motos = Moto.objects.filter(Q(type_model__icontains=query) | Q(brand__name__icontains=query) | Q(categorie__name__icontains=query)) 
        equipements = Equipement.objects.filter(name__icontains=query)
        for elt in equipements:
            if elt.categorie == 'Accéssoire' or elt.categorie.parent_category == 'Accéssoire':
                accessoires.append(elt)
            else:
                pieces.append(elt)

    

   
   #Formulaire de recherche pour les moto et tricycle
    if marque:
        motos = motos.filter(brand__name__icontains=marque) 
    if marque_piece:
        pieces = pieces.filter(moto_cible__brand__name__icontains=marque_piece)
    if type:
        motos = motos.filter(categorie__name__icontains=type) 
    if type_accessoire:
        accessoires = accessoires.filter(categorie__name__icontains=type_accessoire)
    if gamme:
        motos = motos.filter(usage__icontains=gamme)
    if prix_max:
        motos = motos.filter(price__lte=prix_max)
        accessoires = accessoires.filter(price__lte=prix_max)
    if year:
        motos = motos.filter(annee=year)
        pieces = pieces.filter(moto_cible__annee=year)
    if modele:
        pieces = pieces.filter(moto_cible__type_model=modele)
    
    print(pieces)

    context = { 
                'motos': motos,
                'accessoires': accessoires,
                'pieces': pieces,
                'brands': brands,
                'type_accessoires': type_accessoires
               }

    return render(request, 'store/boutique.html', context)

#filtre moto
def filtre_moto(request):
    marque = request.GET.get('marque')
    marque_piece = request.GET.get('marque_piece')
    type = request.GET.get('type') 
    year = request.GET.get('year')
    prix_max = request.GET.get('prix')
    gamme = request.GET.get('gamme')

    motos = Moto.objects.all()  


    if marque:
        motos = motos.filter(brand__name__icontains=marque) 
    if gamme:
        motos = motos.filter(usage__icontains=gamme)
    if marque_piece:
        pieces = pieces.filter(moto_cible__brand__name__icontains=marque_piece)
    if type:
        motos = motos.filter(categorie__name__icontains=type) 
    if year:
        motos = motos.filter(annee=year)
    if prix_max:
        motos = motos.filter(price__lte=prix_max)
     
    motos_list = [
        {
            'id': moto.id,
            'brand': moto.brand.name,
            'type_model': moto.type_model,
            'prix' : moto.price,
            'categorie': moto.categorie.name,
            'image': moto.image.url,
            'annee': moto.annee,
            'gamme': moto.usage
        }
        for moto in motos
    ] 
    return JsonResponse({'motos': motos_list})


#filtre accessoires
def filtre_accessoire(request):
    type_accessoire = request.GET.get('accessoire')
    prix_max = request.GET.get('prix')

    accessoires = Equipement.objects.filter(Q(categorie__name__icontains='accéssoires') | Q(categorie__parent_category__name__icontains='accéssoires'))

    if type_accessoire:
        accessoires = accessoires.filter(categorie__name__icontains=type_accessoire)
    if prix_max:
        accessoires = accessoires.filter(price__lte=prix_max)

    accessoire_list = [
        {
            'id': accessoire.id,
            'name': accessoire.name,
            'prix': accessoire.price,
            'categorie': accessoire.categorie.name,
            'image': accessoire.image.url

        }
        for accessoire in accessoires
    ]
    print("\n\nLes accessoires du filter\n\n")
    print(accessoire_list)
    return JsonResponse({'accessoires': accessoire_list})


def filtre_piece(request): 
    marque_piece = request.GET.get('marque_piece')
    modele = request.GET.get('modele')
    year = request.GET.get('year')

    pieces = Equipement.objects.filter(Q(categorie__name__icontains='pièce') | Q(categorie__parent_category__name__icontains='pièce'))
    
    if marque_piece:
        pieces = pieces.filter(moto_cible__brand__name__icontains=marque_piece)
        print("Hello")
        print(pieces)
    if modele:
        pieces = pieces.filter(moto_cible__type_model=modele)
    if year: 
        pieces = pieces.filter(moto_cible__annee=year)

    pieces_list = [
        {
            'id': piece.id,
            'name': piece.name,
            'prix': piece.price,
            'categorie': piece.categorie.name,
            'image': piece.image.url

        }
        for piece in pieces
    ]
    print("\n\nLes accessoires du filter\n\n")
    print(pieces_list)
    return JsonResponse({'pieces': pieces_list})

 
#fonction qui affiche les détails sur les motos et le tricycles
def details(request, moto_id):
    #on verifie si l'objet est une  

    moto = get_object_or_404(Moto, id=moto_id)  
    #moto_images = moto.images.all()
    similars = Moto.objects.filter(categorie= moto.categorie).exclude(id=moto.id)[:5] 
    variantes = ProductVariation.objects.filter(product=moto)
    
     
    context = {'moto':moto, 
               'variantes': variantes,
               #'moto_images': moto_images,
               'similars':similars
            }

        
    return render(request, 'store/details.html', context)


def details_item(request, item_id):
    #on verifie si l'objet est une 
    #les catégories pour le menu de navigation 
 
    item = get_object_or_404(Equipement, id=item_id) 
    item_images = Images.objects.filter(product=item)
    similars = Equipement.objects.filter(categorie= item.categorie).exclude(id=item.id)[:5]
     
    #on récupère les variantes du produit
    variantes = ProductVariation.objects.filter(product=item) 
    variantes = variantes.values('size').distinct()

    context = {'item':item, 
               'item_images': item_images,
               'variantes': variantes,
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
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitemequipement_set.all()  
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    for item in items:
        pass
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def panier_moto(request):
    return render(request, 'store/panier-moto.html')

def checkout(request): 
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitemequipement_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body) #we load the json data sended in update_item url in the cart.js file
    productId = data['productId']
    action = data['action']

    print('Action:',action)
    print('productId:', productId)

    customer = request.user.customer
    product = Equipement.objects.get(id=productId)
    #now we want to get order of the customer or create it if it doesn't exist
    order, created = Order.objects.get_or_create(customer=customer, complete=False)  

    #Now we create an OrderItem for the order we have created
    #we get_or_create because we need to change the value of the orderItem if it
    #already exist we will add or substract the quantity of product
    orderItem, created = OrderItemEquipement.objects.get_or_create(order=order, equipement=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    if orderItem.quantity == 0:
        orderItem.delete()
        
    return JsonResponse('Item was added', safe=False)


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