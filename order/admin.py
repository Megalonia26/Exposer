from django.contrib import admin

# Register your models here.
from .models import LikedItem

@admin.register(LikedItem)
class LikedModels(admin.ModelAdmin):
    list_display = ["id", "item", "liked"]