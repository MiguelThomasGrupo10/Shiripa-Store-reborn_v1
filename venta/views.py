from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventario,Categoria,Plataforma

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


# ------------------------- INVENTARIO -------------------------------


def lista_inventario(request):
    lista_inventario = Inventario.objects.raw("SELECT * FROM venta_inventario")
    context = {"inventario":lista_inventario}
    return render(request,'venta/inventario/inventario_list.html',context)

def agregar_inventario(request):
    if request.method != "POST":
        lista_categoria = Categoria.objects.all()
        lista_plataforma = Plataforma.objects.all()
        context={"categoria":lista_categoria,"plataforma":lista_plataforma}
        return render(request,'venta/inventario/inventario_add.html',context)
    else:
        nombre_juego = request.POST["game"]
        categoria = request.POST["categoria"]
        plataforma = request.POST["plataforma"]
        valor = request.POST["value"]
        licencias = request.POST["cantidad"]

        objCategoria = Categoria.objects.get(Id_categoria = categoria)
        objPlataforma = Plataforma.objects.get(Id_plataforma = plataforma)

        objInventario = Inventario.objects.create(
            Id_plataforma = objPlataforma,
            Id_categoria = objCategoria,
            nombre_juego = nombre_juego,
            valor = valor,
            stock = licencias)
            
        objInventario.save()
        lista_plataforma = Plataforma.objects.all()
        lista_categoria = Categoria.objects.all()
        context = {"mensaje":"Se guardó el juego al inventario","categoria":lista_categoria,"plataforma":lista_plataforma}
        return render(request,'venta/inventario/inventario_add.html',context)

def eliminar_inventario(request,pk):
    context={}
    try:
        inventario = Inventario.objects.get(Id_juego=pk)

        inventario.delete()
        mensaje = "Se eliminó inventario"
        lista_inventario = Inventario.objects.all()
        context={"inventario":lista_inventario, "mensaje":mensaje}
        return render(request,'venta/inventario/inventario_list.html',context)
    
    except:
        mensaje = "NO se elimino imventario"
        lista_inventario = Inventario.objects.all()
        context={"inventario":lista_inventario, "mensaje":mensaje}
        return render(request,'venta/inventario/inventario_list.html',context)

def buscar_inventario(request,pk):
    if pk != "":
        inventario = Inventario.objects.get(Id_juego=pk)
        lista_categoria = Categoria.objects.all()
        context={"inventario":inventario, "categoria":lista_categoria}
        if Inventario:
            return render(request,'venta/inventario/inventario_edit.html',context)
        else:
            context = {"mensaje":"El juego no existe"}
            return render(request,'venta/inventario/inventario_list.html',context)

def actualizar_inventario(request):
    if request.method == "POST":
        nombre_juego = request.POST["game"]
        categoria = request.POST["category"]
        plataforma = request.POST["plataform"]
        valor = request.POST["value"]
        licencias = request.POST["cantidad"]
    
        objCategoria = Categoria.objects.get(Id_categoria = categoria)
        objPlataforma = Plataforma.objects.get(Id_plataforma = plataforma)

        objInventario = Inventario()
        objInventario.nombre_juego = nombre_juego
        objInventario.Id_categoria = objCategoria
        objInventario.Id_plataforma = objPlataforma
        objInventario.valor = valor
        objInventario.stock = licencias

        objInventario.save()
        lista_plataforma = Plataforma.objects.all()
        lista_categoria = Categoria.objects.all()
        context = {"mensaje":"Se actualizó inventario","categoria":lista_categoria,"plataforma":lista_plataforma}
        return render(request,'venta/inventario/inventario_edit.html',context)

    else:
        lista_inventario = Inventario.objects.all()
        context = {"inventario": lista_inventario}
        return render(request,'venta/inventario/inventario_list.html',context)

