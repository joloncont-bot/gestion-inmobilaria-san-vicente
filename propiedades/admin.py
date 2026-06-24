from django.contrib import admin
from .models import Propiedad, FotoPropiedad, Contacto, SolicitudVisita

class FotoPropiedadInline(admin.TabularInline):
    model = FotoPropiedad
    extra = 3

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'tipo_operacion', 'tipo_propiedad', 'estado', 'precio', 'destacada')
    list_filter = ('tipo_operacion', 'tipo_propiedad', 'estado', 'destacada')
    search_fields = ('codigo', 'titulo', 'comuna', 'direccion')
    inlines = [FotoPropiedadInline]

admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(Contacto)
admin.site.register(SolicitudVisita)