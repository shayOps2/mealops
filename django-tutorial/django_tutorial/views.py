"""
To render html Web Pages
"""
from recipes.models import Recipe
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    recipe_qs = Recipe.objects.all()  # Fetch all Recipe objects

    context = {
        "object_list": recipe_qs,  # Pass the queryset to the template
    }
    return render(request, "home-view.html", context)  