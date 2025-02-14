from django.db import models
from django.contrib.auth.models import User  # Using the Django's user table
# Create your models here.

# These fields will be created into the selected database by Django


class Category(models.Model):
    name = models.CharField(max_length=65)

    # This function returns the category name in the admin area instead of the object ID.
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    # Add the date in the moment of the recipe creation
    created_at = models.DateTimeField(auto_now_add=True)
    # Add the date when the update occurs
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/cover/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    # Using the Django's user table
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    # This function returns the category name in the admin area instead of the object ID.
    def __str__(self):
        return self.title
