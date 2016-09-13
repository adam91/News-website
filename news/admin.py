from django.contrib import admin
from news.models import Category, Article, Comment

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'text', 'source', 'photo']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
