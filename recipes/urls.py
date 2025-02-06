# To better manage Django files, it is advisable to create a URLS.py file inside the app to work with.
# That way you can include these files in the urls.py file at the root of the project.
# It helps to make the code more cohesive.

from django.urls import path
# Must import views from app recipes
from . import views

# app_name creates shortcut to recipes-recipe

app_name = 'recipes'


urlpatterns = [
    # Is possible to call the page by using the given name
    path('', views.home, name="home"),
    # Passe the recipe ID to render the recipe
    # Using the app_name described above.
    path('recipes/<int:id>/', views.recipe, name="recipe"),

]
