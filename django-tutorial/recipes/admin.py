from django.contrib import admin

# Register your models here.
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp', 'slug']
    search_fields = ['title', 'content', 'timestamp']

admin.site.register(Recipe, RecipeAdmin)