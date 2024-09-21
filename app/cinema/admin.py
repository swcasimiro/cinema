from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Index, Category, Video, Comment

admin.site.register(Index)
admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'season')}

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cat', 'title')}


