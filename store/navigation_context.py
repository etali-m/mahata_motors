from .models import Categorie

def navigation_categories(request):
    categories = Categorie.objects.filter(parent_category=None).prefetch_related('sous_categories__produits')
    return {'categories': categories}
