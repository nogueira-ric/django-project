from django.test import TestCase
from django.urls import reverse,resolve
from recipes import views

class RecipeURLSTest(TestCase):
   
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url,'/')
    
    def test_recipe_category_url_is_correct(self):
        recipe_url = reverse('recipes:category', kwargs=({'category_id':1}))
        self.assertEqual(recipe_url,'/recipes/category/1/')

    def test_recipe_recipe_url_is_correct(self):
        recipe_url = reverse('recipes:recipe', kwargs=({'id':1}))
        self.assertEqual(recipe_url,'/recipes/1/') 



class RecipeViewTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs=({'category_id':1})))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs=({'id':1})))
        self.assertIs(view.func, views.recipe)

    