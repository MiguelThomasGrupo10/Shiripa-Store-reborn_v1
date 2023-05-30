from django.shortcuts import render
from django.http import HttpResponse
from .models import Alumno,Genero

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html")

def nosotros(request):
    return render(request, "nosotros.html")

def carrito(request):
    return render(request, "carrito.html")

def contacto(request):
    return render(request, "contacto.html")

def formRegistro(request):
    return render(request, "formRegistro.html")

def micuenta(request):
    return render(request, "micuenta.html")

def tienda(request):
    return render(request, "tienda.html")
