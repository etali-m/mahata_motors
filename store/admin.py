from django.contrib import admin 
from .models import * 
 

#Pour afficher le formulaire de variante dans le forumlaire de produit
class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 3  # Number of empty variation forms to display initially
 
#Pour afficher le formulaire d'ajout d'images dans le formulaire de produit
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3

class ImageVariationInline(admin.TabularInline):
    model = VariationImages
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariationInline, ProductImageInline]

class VariationAdmin(admin.ModelAdmin):
    inlines = [ImageVariationInline]

admin.site.register(ProductVariation, VariationAdmin) 
admin.site.register(Moto, ProductAdmin) 
admin.site.register(Equipement, ProductAdmin)

admin.site.register(Customer) 
admin.site.register(Categorie)
admin.site.register(Brand)  
admin.site.register(Order)
admin.site.register(OrderItemEquipement)
admin.site.register(OrderItemMoto)
admin.site.register(ShippingAddress) 