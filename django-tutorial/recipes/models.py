from django.db import models
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Add slug field
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return f'/recipes/{self.slug}/'
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate a slug if it doesn't already exist
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Recipe.objects.filter(slug=slug).exists():  # Check for uniqueness
                slug = f"{base_slug}-{counter}"  # Append a numeric suffix
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    quanity = models.CharField(max_length=20)  # 1 1/4
    unit = models.CharField(max_length=50) # pounds, lbs, oz, gram, etc
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True)        