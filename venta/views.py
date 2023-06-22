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

#Listar plataformas
def mostrar_plataformas(request):
    lista_plataformas = Plataforma.objects.all()
    context={"plataformas":lista_plataformas}
    return render(request,'venta/plataforma/plataforma_list.html',context)

#agregar plataformas
def agregar_plataformas(request):
    if request.method == "POST":
        form = PlataformaForm(request.POST)
        if form.is_valid:
            form.save() #insert
            form = PlataformaForm()
            context = {"mensaje": "Se grabo la plataforma", "form": form}
            return render(request,'venta/plataforma/plataforma_add.html',context)
            
    else:
        form = PlataformaForm()
        context = {"form": form}
        return render(request,'venta/plataforma/plataforma_add.html',context)

#eliminar plataformas
def borrar_plataformas(request,pk):
    errores = []
    lista_plataformas = Plataforma.objects.all()
    try:
        plataforma = Plataforma.objects.get(Id_plataforma=pk)
        #Aqui hay que llamar a otra funcion de python que sea una confirmación de lo que borramos.
        if plataforma:
            plataforma.delete() #Delete en la BD
            context={"mensaje": "Plataforma eliminada", "plataformas": lista_plataformas, "errores": errores,}
            return render(request,'venta/plataforma/plataforma_list.html',context)
    except:
        lista_plataformas = Plataforma.objects.all()
        context={"mensaje":"No existe la plataforma", "plataformas": lista_plataformas, "errores": errores,}
        return render(request,'venta/plataforma/plataforma_list.html',context)

#modificar plataformas
def actualizar_plataforma(request, pk):
    try:
        plataforma = Plataforma.objects.get(Id_plataforma=pk)
        context={}
        if plataforma:
            print("Edit encontro la plataforma")
            if request.method == "POST":
                print("edit,es un post")
                form = PlataformaForm(request.POST,instance=plataforma)
                form.save()
                context = {"mensaje": "Se actualizó la plataforma", "form":form, "plataforma":plataforma}
                return render(request, 'venta/plataforma/plataforma_edit.html', context)
            else:
                form = PlataformaForm(instance=plataforma)
                mensaje = ""
                context = {"mensaje": mensaje, "form":form, "plataforma":plataforma}
                return render(request, 'venta/plataforma/plataforma_edit.html', context)
    except:
        mensaje = "No existe la plataforma"
        lista_plataformas = Plataforma.objects.all()
        context = {"mensaje": mensaje, "form":form, "plataforma":lista_plataformas}
        return render(request, 'venta/plataforma/plataforma_list.html', context)


#listar categorias
def mostrar_categorias(request):
    lista_categorias = Categoria.objects.all()
    context={"categorias":lista_categorias}
    return render(request,'venta/categoria/categoria_list.html',context)

#agregar categorias
def agregar_categorias(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid:
            form.save() #insert
            form = CategoriaForm()
            context = {"mensaje": "Se grabo la categoria", "form": form}
            return render(request,'venta/categoria/categoria_add.html',context)
            
    else:
        form = CategoriaForm()
        context = {"form": form}
        return render(request,'venta/categoria/categoria_add.html',context)

#eliminar categorias
def borrar_categorias(request,pk):
    errores = []
    lista_categorias = Categoria.objects.all()
    try:
        categoria = Categoria.objects.get(Id_categoria=pk)
        #Aqui hay que llamar a otra funcion de python que sea una confirmación de lo que borramos.
        if categoria:
            categoria.delete() #Delete en la BD
            context={"mensaje": "Categoria eliminada", "categorias": lista_categorias, "errores": errores,}
            return render(request,'venta/categoria/categoria_list.html',context)
    except:
        lista_categorias = Categoria.objects.all()
        context={"mensaje":"No existe la categoria", "categorias": lista_categorias, "errores": errores,}
        return render(request,'venta/categoria/categoria_list.html',context)

#modificar categorias
def actualizar_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(Id_categoria=pk)
        context={}
        if categoria:
            print("Edit encontro la categoria")
            if request.method == "POST":
                print("edit,es un post")
                form = CategoriaForm(request.POST,instance=categoria)
                form.save()
                context = {"mensaje": "Se actualizó la categoria", "form":form, "categoria":categoria}
                return render(request,'venta/categoria/categoria_edit.html',context)
            else:
                form = CategoriaForm(instance=categoria)
                mensaje = ""
                context = {"mensaje": mensaje, "form":form, "categoria":categoria}
                return render(request, 'venta/categoria/categoria_edit.html', context)
    except:
        mensaje = "No existe la categoria"
        lista_categorias = Categoria.objects.all()
        context = {"mensaje": mensaje, "form":form, "categoria":lista_categorias}
        return render(request, 'venta/categoria/categoria_list.html', context)