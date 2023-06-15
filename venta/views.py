from django.shortcuts import render
from django.http import HttpResponse
from .models import Plataforma, Categoria
from .forms import PlataformaForm, CategoriaForm

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

#modificar categorias



















# #FUNCION LICENCIA ALEATORIA, realiza una funcion aleatoria que utiliza después la boleta
# def generar_codigo_licencia():
#     caracteres_permitidos = string.ascii_uppercase + string.ascii_lowercase + string.digits
#     longitud_codigo = 10
#     codigo_licencia = ''.join(random.choice(caracteres_permitidos) for _ in range(longitud_codigo))
#     return codigo_licencia

#     # Obtener el nombre y valor del juego desde el Inventario hacia Boleta
# def save(self, *args, **kwargs):
#     inventario = Inventario.objects.get(Id_juego=self.Id_inventario_id)
#     self.nombre_juego = inventario.nombre_juego
#     self.valor = inventario.valor
#     super().save(*args, **kwargs)   
    
#     # Obtener el email desde el Usuario hacia Boleta     
    
# def save(self, *args, **kwargs):   
#     usuario = Usuarios.objects.get(id_usuario=self.Id_usuario_id)
#     self.email = usuario.email
#     super().save(*args, **kwargs)
