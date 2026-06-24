from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Propiedad, SolicitudVisita
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def inicio(request):
    destacadas = Propiedad.objects.filter(
    destacada=True,
    estado='Disponible'
    )[:4]
    return render(request, 'propiedades/inicio.html', {
        'destacadas': destacadas
    })

def propiedades(request):
    propiedades = Propiedad.objects.filter(
    estado='Disponible'
    ).order_by('-fecha_publicacion')

    buscar = request.GET.get('buscar', '')
    operacion = request.GET.get('operacion', '')
    comuna = request.GET.get('comuna', '')
    dormitorios = request.GET.get('dormitorios', '')
    precio_max = request.GET.get('precio_max', '')

    if buscar:
        propiedades = propiedades.filter(
            Q(titulo__icontains=buscar) |
            Q(codigo__icontains=buscar) |
            Q(comuna__icontains=buscar) |
            Q(direccion__icontains=buscar)
        )

    if operacion:
        propiedades = propiedades.filter(tipo_operacion=operacion)

    if comuna:
        propiedades = propiedades.filter(comuna__icontains=comuna)

    if dormitorios:
        propiedades = propiedades.filter(dormitorios=dormitorios)

    if precio_max:
        precio_max = precio_max.replace(".", "").replace(",", "").replace(" ", "")

        if precio_max.isdigit():
            propiedades = propiedades.filter(precio__lte=int(precio_max))

    return render(request, 'propiedades/propiedades.html', {
        'propiedades': propiedades
    })


def detalle(request, id):
    propiedad = get_object_or_404(Propiedad, id=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')

        SolicitudVisita.objects.create(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            codigo_propiedad=propiedad.codigo,
            mensaje=mensaje
        )

        asunto = f"Nueva solicitud de visita - {propiedad.codigo}"

        cuerpo = f"""
Nueva solicitud de visita recibida.

Propiedad:
Código: {propiedad.codigo}
Título: {propiedad.titulo}
Operación: {propiedad.tipo_operacion}
Dirección: {propiedad.direccion}
Precio: ${propiedad.precio}

Datos del cliente:
Nombre: {nombre}
Correo: {correo}
Teléfono: {telefono}

Mensaje:
{mensaje}
"""

        send_mail(
            asunto,
            cuerpo,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_DESTINO],
            fail_silently=False,
        )

        messages.success(
                request,
                'Solicitud enviada correctamente. Nos contactaremos contigo a la brevedad.'
        )
        return redirect('detalle', id=propiedad.id)

    return render(request, 'propiedades/detalle.html', {
        'propiedad': propiedad
    })


def contacto(request):
    return render(request, 'propiedades/contacto.html')


def quienes_somos(request):
    return render(request, 'propiedades/quienes_somos.html')


def servicios(request):
    return render(request, 'propiedades/servicios.html')