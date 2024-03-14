from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=("id", "create_date", "update_date")
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)