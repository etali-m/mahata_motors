from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    CUSTOMER = 'CUSTOMER'
    SELLER = 'SELLER'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = (
        (CUSTOMER, 'customer'),
        (SELLER, 'seller'),
        (ADMIN, 'administrator'),
    )

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default=CUSTOMER,)
    # Rendre le champ username facultatif
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Enlever 'email' de REQUIRED_FIELDS
    numero_telephone = PhoneNumberField() #Ajout du champ numero_telephone
