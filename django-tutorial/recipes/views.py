from django.shortcuts import render
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from django.http import Http404
from django.db.models import Q 
from django.forms import modelformset_factory

# Create your views here.
def recipe_detail_view(request, slug=None):
    recipe_obj = None
    if slug is not None:
        try:
            recipe_obj = Recipe.objects.get(slug=slug)
        except Recipe.DoesNotExist:
            raise Http404("Recipe not found")
    context = {
        "object": recipe_obj,
    }
    return render(request, "recipes/detail.html", context=context)

def recipe_search_view(request):
    query = request.GET.get('q')  # Get the search query from the request
    recipe_objects = None
    if query:
        # Search for recipes where the name contains the query (case-insensitive)
        recipe_objects = Recipe.objects.filter(
            Q(name__icontains=query)
        )
    context = {
        "object_list": recipe_objects  # Pass the list of matching recipes to the template
    }
    return render(request, "recipes/search.html", context=context)

@login_required
def recipe_create_view(request):
    RecipeIngredientFormSet = modelformset_factory(RecipeIngredient, fields=('name', 'quantity', 'unit', 'description'), extra=1)
    form = RecipeForm(request.POST or None)
    formset = RecipeIngredientFormSet(request.POST or None, queryset=RecipeIngredient.objects.none())
    context = {
        "form": form,
        "formset": formset
    }
    if form.is_valid() and formset.is_valid():
        recipe_object = form.save(commit=False)
        recipe_object.user = request.user  # Associate the recipe with the logged-in user
        recipe_object.save()
        for ingredient_form in formset:
            if ingredient_form.cleaned_data:  # Avoid saving empty forms
                ingredient = ingredient_form.save(commit=False)
                ingredient.recipe = recipe_object
                ingredient.save()
        context['form'] = RecipeForm() 
        context['formset'] = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())
        context['object'] = recipe_object
        context['created'] = True

    return render(request, "recipes/create.html", context=context)
