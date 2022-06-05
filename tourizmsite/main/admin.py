from django.contrib import admin

# Register your models here.
from .models import TourizmType, TourPlace


class TourizmTypeAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','updated_at','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
admin.site.register(TourizmType,TourizmTypeAdmin)

class TourPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','tourtype', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


admin.site.register(TourPlace, TourPlaceAdmin)

