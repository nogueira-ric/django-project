from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe  # Queryset API


# Create your views here.


def home(request):
    # Rendering web applications.
    # recipes/ points to the path of the templates, such as /recipes or global/.
    # This allows you to reuse files with the same name by simply pointing to the template path.
    # return render(request, 'recipes/pages/home.html', context={'recipes': [make_recipe() for _ in range(10)], })

    # This instuction above was using FAKER, now we are going to get the recipes. Queryset API
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    # Rendering web applications.
    # recipes/ points to the path of the templates, such as /recipes or global/.
    # This allows you to reuse files with the same name by simply pointing to the template path.
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })


def category(request, category_id):
    # As the category ID is a PK in the recipe (templates), you reference it as category__id and pass the category_id field.
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })
