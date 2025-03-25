from django.db import models
from django.utils.text import slugify

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)