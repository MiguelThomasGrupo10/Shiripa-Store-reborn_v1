from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventario

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "venta/index.html")

def nosotros(request):
    return render(request, "venta/nosotros.html")

def carrito(request):
    return render(request, "venta/carrito.html")

def contacto(request):
    return render(request, "usuarios/contacto.html")

def formRegistro(request):
    return render(request, "usuarios/formRegistro.html")

def micuenta(request):
    return render(request, "usuarios/micuenta.html")

def tienda(request):
    return render(request, "venta/tienda.html")
