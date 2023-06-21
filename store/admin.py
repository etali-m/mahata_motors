from django.contrib import admin 
from .models import * 

class AccessoryAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        accessory_category = Categorie.objects.get(name__icontains='Accessoire')
        initial['categorie'] = accessory_category.id
        return initial
    
class MotorBikeAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        moto_category = Categorie.objects.get(name__icontains='Motocylette')
        initial['categorie'] = moto_category.id
        return initial


class TricycleAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        tricycle_category = Categorie.objects.get(name__icontains='Tricycle')
        initial['categorie'] = tricycle_category.id
        return initial




admin.site.register(Customer) 
admin.site.register(Categorie)
admin.site.register(Brand)
admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(MotorBike, MotorBikeAdmin)
admin.site.register(Tricycle, TricycleAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress) 