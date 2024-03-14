"""
URL configuration for primerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from miApp import views
import miApp.views

from django.contrib import admin
from django.urls import path
import miApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', miApp.views.saludo, name="Saludo"),
    path('hola_mundo/', miApp.views.hola_mundo, name= "hola mundo"),
    path('', miApp.views.index, name= "index"),
    path('presentacion/', miApp.views.presentacion, name="Presentacion"),
    path('contacto/', miApp.views.contacto, name="Contacto "),
    path('contacto/<str:nombre>', miApp.views.contacto, name="Contacto "),
    path('contacto/<str:nombre>/<str:apellido>', miApp.views.contacto, name="Contacto"),
    path('tarea/', miApp.views.tarea, name= "tarea"),
    path('pagina/', miApp.views.pagina, name= "pagina"),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', miApp.views.crear_articulo, name ="crear_articulo"),
    path('articulo/', miApp.views.articulo, name="Articulo"),
    path('editar_articulo/<int:id>', miApp.views.editar_articulo, name="Editar Articulo"),
    path('articulos/', miApp.views.articulos, name="Listar"),
    path('delete_articulo/<int:id>', miApp.views.delete_articulo, name="eliminar_sql"),
    path('update_articulo/<str:title>/<int:id>', miApp.views.update_articulo, name="actualizar_sql"),
    path('create_articulo/', miApp.views.create_articulo, name="create"),
    path('save_articulo/', miApp.views.save_articulo, name="save"),
    path('create_full_article/', miApp.views.create_full_articulo, name="create_full"),]
