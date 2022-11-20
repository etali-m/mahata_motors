from django.db import models
from authentication.models import User 

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name


"""
    La classe Product défini un produit avec toutes ses caratéristiques
"""

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank = True)
    stock = models.BooleanField(default=True, null=True, blank=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Brand(models.Model):
    name = models.CharField(max_length=30)
    origine = models.CharField(max_length=30)
    #logo = models.ImageField()


class Moto(Product):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)
    chassis = models.IntegerField()
    cylindre = models.FloatField()
    nbre_vitesse = models.IntegerField(blank=True)
    vignette = models.FloatField()
    type_model = models.CharField(max_length=20)
    poids = models.DecimalField(max_digits = 7, decimal_places = 2)
    tension_batterie = models.DecimalField(max_digits = 7, decimal_places=2)
    puissance_admin = models.FloatField()
    capacite_recervoir = models.DecimalField(max_digits = 5, decimal_places = 2)
    nbre_place = models.IntegerField()
    coulour = models.CharField(max_length=20)
    garantie = models.DateField()




    class Meta:
        abstract = True


class Accessory(Product):
    color = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()


"""
    La classe Tricycle permet de définir la structure d'un tricycle
"""
class Tricycle(Moto):
    wheels_number = models.IntegerField(default=3)


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

    motor_warranty = models.DateField()
    usage = models.CharField(max_length=30, choices=USAGE_CHOICES)




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


    def __str__(self):
        return str(self.id)

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

    def __str__(self):
        return self.address