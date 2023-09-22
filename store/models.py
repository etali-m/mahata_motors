from django.db import models
from authentication.models import User 
from django.utils.text import slugify
from autoslug import AutoSlugField   

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=20)

    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name

"""
La classe Catégorie défini la catégorie d'un produit
"""
class Categorie(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank = True)
    description = models.TextField(default="No description", null=True, blank=True)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='sous_categories')
    slug = AutoSlugField(unique=True, populate_from='name')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categorie, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

"""
    La classe Product défini un produit avec toutes ses caratéristiques
"""
 
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', null=True, blank = True)
    stock = models.BooleanField(default=True, null=True, blank=False)
    is_on_sale = models.BooleanField(default=False) #si un produit est on solde
    sale_price = models.IntegerField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1, related_name='produits')
    description = models.TextField(blank=True, null=True, default="No description") 


    def __str__(self):
        return self.name

    def get_sale_price(self):
        if self.is_on_sale:
            return self.sale_price
        else:
            return None

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


""" 
    Cette classe permet de définir les images pour un produit car un produit peut avoir plusieurs images
"""

class Images(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='product_images/')


    def __str__(self):
        return self.title



class Brand(models.Model):
    name = models.CharField(max_length=30)
    origine = models.CharField(max_length=30)
    logo = models.ImageField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Marques'

    def __str__(self):
        return self.name

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Moto(Product):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)
    chassis = models.IntegerField()
    cylindre = models.FloatField()
    nbre_vitesse = models.IntegerField(blank=True)
    vignette = models.BooleanField(default=False)
    type_model = models.CharField(max_length=20)
    poids = models.DecimalField(max_digits = 7, decimal_places = 2)
    tension_batterie = models.DecimalField(max_digits = 7, decimal_places=2)
    puissance_admin = models.FloatField()
    capacite_recervoir = models.DecimalField(max_digits = 5, decimal_places = 2)
    nbre_place = models.IntegerField()
    coulour = models.CharField(max_length=20)
    




    class Meta:
        abstract = True


class Accessory(Product):
    color = models.CharField(max_length=20, blank=True, null=True) 

    class Meta:
        verbose_name_plural = 'Accessoires'



"""
    La classe Tricycle permet de définir la structure d'un tricycle
"""
class Tricycle(Moto):
    wheels_number = models.IntegerField(default=3) #il faut mettre les nombres de roues par 
    
    class Meta:
        verbose_name_plural = 'Tricycles'


"""
    La class MotorBike permet de définir la structure d'une motocyclette
"""
class MotorBike(Moto):
    VILLE = 'VILLE'
    COMMERCIAL = 'COMMERCIAL'
    AVENTURE = 'AVENTURE'

    USAGE_CHOICES = (
        (VILLE, 'ville'),
        (COMMERCIAL, 'commercial'),
        (AVENTURE, 'aventure')
    )

    motor_warranty = models.IntegerField(null=True, blank=True)
    usage = models.CharField(max_length=30, choices=USAGE_CHOICES)

    class Meta:
        verbose_name_plural = 'Motocylettes'



"""
    La classe Order permet de définir une commande
"""
class Order(models.Model):
    ATTENTE = 'ATTENTE'
    EN_COURS = 'EN COURS'
    LIVRE = 'LIVRE'


    STATUS_CHOICES = (
        (ATTENTE, 'attente'), 
        (EN_COURS, 'En cours de livraison'),
        (LIVRE, 'Livré')
    )

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add =True)
    complete = models.BooleanField(default = False)
    transaction_id = models.CharField(max_length = 100, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = 'Commandes'


    def __str__(self):
        return str(self.id)

    #le prix total d'une commande
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
        
    #la quantité totale d'article dans le panier
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

"""
    cette classe permet de définir une ligne de commande
    une commande peut avoir plusieur ligne de commande et une 
    ligne de commande concerne un produit
"""
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


""" 
    La classe ShippingAddress contient toute les informations sur 
    l'adresse de livraison d'une commande.
"""
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    quater = models.CharField(max_length=200, null=False)
    codepostal = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Adresses de livraison'

    def __str__(self):
        return self.address