from django.test import TestCase
from django.urls import reverse,resolve 
from recipes import views
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# Create your tests here.

class RecipeViwerTest(TestCase):
    
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')