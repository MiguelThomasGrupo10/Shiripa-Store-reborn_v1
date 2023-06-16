from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name = 'index'),
    path('index/', views.index,name = 'index'),
    path('nosotros/', views.nosotros),
    path('carrito/',views.carrito),
    path('micuenta/',views.micuenta),
    path('tienda/',views.tienda),
    path('contacto/',views.contacto),
    path('formRegistro/',views.formRegistro),

    path('inventario_lista',views.lista_inventario,name='lista_inventario'),
    path('inventarioAdd',views.agregar_inventario,name='inventarioAdd'),
    path('borrarInventario/<str:pk>',views.eliminar_inventario,name='inventario_del'),
    path('buscarInventario/<str:pk>',views.buscar_inventario,name='inventario_findEdit'),
    path('actualizarInventario',views.actualizar_inventario,name='actualizar_inventario'),
]