from django.contrib import admin

# Register your models here.
from .models import TourizmType, TourPlace, Category, Shop


class TourizmTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(TourizmType, TourizmTypeAdmin)


class TourPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tourtype', 'description', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published',)


admin.site.register(TourPlace, TourPlaceAdmin)


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Shop, ShopAdmin)
