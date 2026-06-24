from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('servicios/', views.servicios, name='servicios'),
    path('propiedades/', views.propiedades, name='propiedades'),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
    path('contacto/', views.contacto, name='contacto'),
]