from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="")
    public = models.BooleanField(verbose_name="¿publicado?")
    create_date = models.DateTimeField(auto_now_add = True, verbose_name="Fecha creación")
    update_date =models.DateField(auto_now =True, verbose_name="Fecha actualización")
    class Meta:
        # db_table=""
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        ordering = ['-id']
    def __str__(self):
        if self.public:
            publico ="(Publicado)"
        else:
            publico ="(Privado)"
        return f"{self.id} - {self.title} ----> {publico}"

class Category(models.Model):
    name = models.CharField(max_length=110, verbose_name="Nombre")
    description = models.CharField(max_length=250, verbose_name="Descripción")
    create_date = models.DateField(verbose_name="Fecha Creación")
    class Meta:
    # db_table=""
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
    def __str__(self):
        return f"{self.id} ---> {self.name}"
