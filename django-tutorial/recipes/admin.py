from django.contrib import admin

# Register your models here.
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'timestamp', 'slug']
    search_fields = ['name', 'description', 'timestamp']

admin.site.register(Recipe, RecipeAdmin)