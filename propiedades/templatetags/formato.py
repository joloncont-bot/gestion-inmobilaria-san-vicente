from django import template

register = template.Library()

@register.filter
def precio_chileno(valor):
    try:
        valor = int(valor)
        return f"{valor:,}".replace(",", ".")
    except:
        return valor