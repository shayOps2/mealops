from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance', None)  # Get the current instance
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Recipe.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This name is already in use. Please pick another name.")
        return name