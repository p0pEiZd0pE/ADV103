from django.contrib import admin
from .models import Tag, Category, Article


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category_name',)
    list_display = ('category_name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('headline', 'categories',)
    list_display = ('headline', 'categories',)