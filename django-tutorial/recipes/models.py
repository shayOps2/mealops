from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/recipes/{self.slug}/'
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate a slug if it doesn't already exist
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Recipe.objects.filter(slug=slug).exists():  # Check for uniqueness
                slug = f"{base_slug}-{counter}"  # Append a numeric suffix
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)