from django.contrib import admin

from .models import BlogModels

@admin.register(BlogModels)
class BlogManager(admin.ModelAdmin):
    list_display = ["id", "poster", "title", "created"]