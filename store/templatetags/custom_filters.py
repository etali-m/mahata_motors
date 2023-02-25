from django import template

register = template.Library()

@register.filter(name="separate_by_space")
def separate_by_space(value):
    value = str(value)
    return " ".join(value[i:i+3] for i in range(0, len(value), 3))