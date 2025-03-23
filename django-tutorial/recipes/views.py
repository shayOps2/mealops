from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm

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

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        recipe_object = form.save()
        context['form'] = RecipeForm() 
        context['object'] = recipe_object
        context['created'] = True
        
    return render(request, "recipes/create.html", context=context)
