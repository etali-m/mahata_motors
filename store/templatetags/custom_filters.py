from django import template

register = template.Library()

@register.filter(name="separate_by_space")
def separate_by_space(value):
    value = str(value)
    reversed_value = value[::-1]  # Inverser la chaîne de caractères
    reversed_chunks = [reversed_value[i:i+3] for i in range(0, len(reversed_value), 3)]
    result = " ".join(reversed_chunks)
    return result[::-1]  # Inverser à nouveau pour obtenir l'ordre original
