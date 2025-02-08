from django.contrib import admin
from .models import Category, Recipe

# Register your models here.
# The models registered here will be available at admin area.


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
