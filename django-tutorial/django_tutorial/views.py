"""
To render html Web Pages
"""
from django.http import HttpResponse
from recipes.models import Recipe
from django.template.loader import render_to_string

def home_view(request, *args, **kwrgs):
    recipe_obj = Recipe.objects.get(id=2)
    recipe_qs = Recipe.objects.all()

    context = {
        "object_list": recipe_qs,
        "title": recipe_obj.title,
        "content": recipe_obj.content,
        "id": recipe_obj.id,
    }
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)