from django.contrib import admin

from .models import Contents, Category, Images


# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("title",)


class ContentModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_date', 'modified_date', 'main_text', 'published_date')
    prepopulated_fields = {"slug": ('title',)}
    list_editable = ['main_text']
    search_fields = ['title', ]


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Contents, ContentModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Images, ImageModelAdmin)
