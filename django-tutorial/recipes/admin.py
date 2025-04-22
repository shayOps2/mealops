from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeIngredient

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0  # Number of empty forms to display

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    search_fields = ['name', 'description', 'timestamp']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)