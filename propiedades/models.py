from django.db import models

class Propiedad(models.Model):

    TIPO_OPERACION = [
        ('Venta', 'Venta'),
        ('Arriendo', 'Arriendo'),
    ]

    TIPO_PROPIEDAD = [
        ('Casa', 'Casa'),
        ('Terreno', 'Terreno'),
        ('Parcela', 'Parcela'),
        ('Sitio', 'Sitio'),
        ('Local Comercial', 'Local Comercial'),
    ]

    ESTADO_PROPIEDAD = [
        ('Disponible', 'Disponible'),
        ('Reservada', 'Reservada'),
        ('Vendida', 'Vendida'),
        ('Arrendada', 'Arrendada'),
    ]

    codigo = models.CharField(max_length=20, unique=True, blank=True, null=True)
    titulo = models.CharField(max_length=150)
    tipo_operacion = models.CharField(max_length=20, choices=TIPO_OPERACION)
    tipo_propiedad = models.CharField(max_length=50, choices=TIPO_PROPIEDAD)
    estado = models.CharField(max_length=20, choices=ESTADO_PROPIEDAD, default='Disponible')
    precio = models.IntegerField()
    comuna = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    dormitorios = models.IntegerField(default=0)
    banos = models.IntegerField(default=0)
    metros_cuadrados = models.IntegerField(default=0)
    descripcion = models.TextField()
    destacada = models.BooleanField(default=False)
    imagen_principal = models.ImageField(upload_to='propiedades/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"


class FotoPropiedad(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='propiedades/galeria/')

    def __str__(self):
        return f"Foto de {self.propiedad.codigo}"


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class SolicitudVisita(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    codigo_propiedad = models.CharField(max_length=20)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visita {self.codigo_propiedad} - {self.nombre}"