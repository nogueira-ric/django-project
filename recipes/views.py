from django.shortcuts import render
from utils.recipes.factory import make_recipe
# Create your views here.

def home(request):
    #Rendering web applications. 
    #recipes/ points to the path of the templates, such as /recipes or global/.
    #This allows you to reuse files with the same name by simply pointing to the template path.
    return render(request,'recipes/pages/home.html', context={'recipes': [make_recipe() for _ in range(10)], })


def recipe(request, id):
    #Rendering web applications. 
    #recipes/ points to the path of the templates, such as /recipes or global/.
    #This allows you to reuse files with the same name by simply pointing to the template path.
    return render(request,'recipes/pages/recipe-view.html', context={'recipe': make_recipe(),})