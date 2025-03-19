from django.shortcuts import render
from .models import Recipe
# Create your views here.
def recipe_detail_view(request, id=None):
    recipe_obj = None
    if id is not None:
        recipe_obj = Recipe.objects.get(id=id)
    context = {
        "object": recipe_obj,
    }
    return render(request, "recipes/detail.html", context=context)

def recipe_search_view(request):
    try:
        query = int(request.GET.get('q'))
    except:
        query = None

    recipe_obj = None
    if query is not None:
        recipe_obj = Recipe.objects.get(id=query)
    context = {
        "object": recipe_obj
    }
    return render(request, "recipes/search.html", context=context)

def recipe_create_view(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        rec_object = Recipe.objects.create(title=title, content=content)
        context['object'] = rec_object
        context['created'] = True
        
    return render(request, "recipes/create.html", context=context)
