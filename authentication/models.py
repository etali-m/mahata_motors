from django.db import models
from django.contrib.auth.models import AbstractUser

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