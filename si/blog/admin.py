from django.contrib import admin
from blog.models import Article


admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','date']