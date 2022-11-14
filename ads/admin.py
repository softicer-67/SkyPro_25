from django.contrib import admin
from .models import Cat, Ads


@admin.register(Cat)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Ads)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'description']
    search_fields = ('name', 'price',)
