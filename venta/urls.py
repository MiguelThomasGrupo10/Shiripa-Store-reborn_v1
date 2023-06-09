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

    path('listar_plataformas',views.mostrar_plataformas,name='crud_plataformas'),
    path('agregar_plataformas',views.agregar_plataformas,name='plataformasAdd'),
    path('borrar_plataformas/<str:pk>',views.borrar_plataformas,name='plataformas_del'),
    path('actualizar_plataformas/<str:pk>',views.actualizar_plataforma,name='plataformas_edit'),


    path('listar_categorias',views.mostrar_categorias,name='crud_categorias'),
    path('agregar_categorias',views.agregar_categorias,name='categoriasAdd'),
    path('borrar_categorias/<str:pk>',views.borrar_categorias,name='categorias_del'),
    path('actualizar_categorias/<str:pk>',views.actualizar_categoria,name='categorias_edit'),

    path('listar_inventario', views.lista_inventario,name='crud_inventario'),
    path('agregar_inventario', views.agregar_inventario,name='inventarioAdd'),






]