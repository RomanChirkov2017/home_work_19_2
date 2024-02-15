from django.contrib import admin

from catalog.models import Category, Product, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'version_number', 'name', 'product', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('version_number', 'name', 'product')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_date', 'view_count', 'is_published',)
    search_fields = ('name',)

