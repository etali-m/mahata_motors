from django.contrib import admin 
from .models import * 

admin.site.register(Customer) 
admin.site.register(Categorie)
admin.site.register(Brand)
admin.site.register(Accessory)
admin.site.register(MotorBike)
admin.site.register(Tricycle)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress) 