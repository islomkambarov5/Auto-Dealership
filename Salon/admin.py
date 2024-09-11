from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from django.contrib.admin.decorators import register


# Register your models here.

class GalleryInline(admin.TabularInline):
    fk_name = 'car'
    model = Gallery
    extra = 0


@admin.register(Cars)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'brand', 'model', 'quantity', 'price', 'engine', 'color', 'created_at', 'get_photo')
    list_editable = ('quantity', 'price', 'engine', 'color')  # Какие поля можно редактировать
    list_display_links = ('brand', 'model')
    list_filter = ('brand', 'price')
    prepopulated_fields = {'slug': ('brand', 'model')}
    inlines = [GalleryInline]

    # Метод который вернёт в Админку картинку товара
    def get_photo(self, obj):
        if obj.images:
            try:
                return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75">')
            except:
                return '-'
        else:
            return '-'

    get_photo.short_description = 'Photo'
