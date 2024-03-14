from django.shortcuts import render, HttpResponse, redirect
from miApp.models import Article
from django.db import connection
from django.db.models import Q
from miApp.forms import FormArticulo
from django.contrib import message

# Create your views here.
def hola_mundo (request):
    #return HttpResponse(layout + "Hola mundo desde de Django")
    return render(request, 'hola_mundo.html')
    
def saludo(request):

        #return redirect ('Contacto', nombre= "Neylliber", apellido= "Lopez")
        return render(request, 'saludo.html')

    #return HttpResponse("""
    #                    <h1>Saludo de Bienvenida<h1/>
    #                   <h2>Bienvenidos al SENA Tolima<h2/>
    #                  """)

def index(request):
    template ="""
                <h1> Inicio <h1/>
                <h3><p> Años desde el 2024 hasta el año 2050</p>
                <ul>
                """
    year = 2024
    while year <= 2050:
        template += f" <li> {year} "
        if year % 2 == 0 :
            template += " Año par"

        if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
            template += " Año bisiesto "

        template += "</li>"
        year += 1
    
    template += "</lu> <h3/>"
    #return HttpResponse(layout + template)

    return render(request, 'index.html' ,{
        'mi_variable' :'soy un dato que esta en la vista ', 
        'title': 'Inicio de Sitio',
        'titulo': 'Pagina de Inicio Sena', 
        'name': 'nombre',
        'mi_lista': 'mi_lista'
        })

def presentacion(request):
    #return HttpResponse("""
    #                    <h2>Hola mi nombre es Neylliber Melissa Lopez Higinio</h2>
    #                    <h3>Mi correo es neylliberlopez@gmail.com</h3>
    #                    <h4>Mi numero de telefono es : 3214341900</h4>
    #                    """)

    return render(request, 'presentacion.html')

def contacto(request,nombre="",apellido=""):
    aprendiz=""
    if nombre and apellido:
        aprendiz = "<h2>Nombre completo: </h2>"
        aprendiz = f"<h3>{nombre} {apellido}</h3>"
    elif nombre  :
        aprendiz = "<h2>Nombre: </h2>"
        aprendiz = f"<h3> {nombre} </h3>"
    
    
    #return HttpResponse(layout + f"<h2>Contacto: </h2>" + aprendiz)
    return render(request, 'contacto.html')

def tarea(request):
    # Lista de nombres
    nombres = ["Neylliber", "Melissa", "Vanesa", "Stiven", "Nicol"]

    # Contar cuántos nombres comienzan con la letra 'N'
    contador_l = 0
    for nombre in nombres:
        if nombre.startswith('N'):
            contador_l += 1

    return render(request, 'tarea.html', {
        'nombres': nombres,
        'contador_l': contador_l
    })  
def pagina(request,redirigir = 0):
    if redirigir == 1:
        return redirect('contacto', nombre ="Ana", apellidos = "Perez")
    return render(request,'pagina.html' , {'texto':'Este es mi texto', 'lista':['uno','dos','tres'],})

def crear_articulo(request,title,content,public):
    articulo = Article(
        title = title,
        content = content,
        public = public,
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.title} - {articulo.content}")

def articulo (request):
    try:
        articulo = Article.objects.get(pk=7,public=False)
        response = f"Articulo Consultado: {articulo.title}- {articulo.content} - Estado:{articulo.public} "
    except:
        response="<strong>Articulo no encontrado</strong>"
    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=8)
    articulo.title = "El principito"
    articulo.public = True
    articulo.save()
    return HttpResponse(f"El articulo {articulo.id} de nombre: {articulo.title} ha sido actualizado y su estado es: {articulo.public}")

def articulos(request):
    #articulos = Article.objects.order_by('id')
    #articulos = Article.objects.filter(title= "Articulo 4")
    #articulos = Article.objects.filter(public= True,id=1)
    #Lookups en Django
    # articulos =Article.objects.filter(title__contains="articulo")
    # articulos =Article.objects.filter(title__exact="articulo")
    # articulos =Article.objects.filter(title__iexact="articulo 4")
    #articulos = Article.objects.filter(id__gt=9)
    #articulos =Article.objects.filter(id__lte=16)
    #articulos =Article.objects.filter(id__in=[10,11,12])
    #articulos =Article.objects.filter(id__in=[1,6,8])
    #articulos =Article.objects.filter(id__range=(7,9))
    articulos =Article.objects.filter(
                                title__contains ="Art",

                                ).exclude(
                                    public= True
                                )
    articulos= Article.objects.raw("SELECT * FROM miApp_article WHERE content like 'L%' AND public = 1")
    articulos= Article.objects.filter(
        Q(title__contains = "a")|Q(public = 0)
    )
   
    return render(request, 'articulos.html', {
        'articulos':articulos
    })
    return HttpResponse()

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('Listar')

def delete_articulo(request, id):
    
    Temp = (f"DELETE FROM miApp_article WHERE id = %s")
    with connection.cursor() as cursor:
        cursor.execute(Temp, [id])

        articulos= Article.objects.all()
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def update_articulo(request, title, id):
    Temp = (f"UPDATE miApp_article SET title = %s WHERE id = %s")
    with connection.cursor() as cursor:
        cursor.execute(Temp,[title, id] )
        articulos= Article.objects.all()
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def actualizar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "Articulo 13"
    articulo.public = True
    articulo.content = ""
    articulo.save()
    return redirect('Listar')

def save_articulo(request):
    
    if request.method == "POST":
        title = request.POST["title"]
        if len(title)<=5:
            return HttpResponse(f"El Titulo debe ser mayor a 5 caracteres")
        
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title = title,
            content = content,
            public = public,
            )
        articulo.save()
        return HttpResponse(f"Articulo Creado: {articulo.title}- {articulo.content}")
    else:
        return HttpResponse(f"Articulo no fue creado")

def create_articulo(request):
    return render(request,'create_articulo.html')


def create_full_articulo(request):
    if request.method == 'POST':
        formulario = FormArticulo(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form.get(public)
            
            articulo = Article(
                title = title,
                content = content,
                public = public,
            )
            articulo.save()

            message.sucess(request, f'El articulo {articulo.id} se ha guardado satisfactoriamente ')   

            return render(request, 'articulo.html',{
                'titulo':'Guardado el articulo con Exito',
                'icono': 'success',
                'boton' : 'Aceptar',
                'articulos' : articulos
            })   
    else:
        formulario = FormArticulo()
    return render(request, 'create_full_articulos.html',{
        'form':formulario
})