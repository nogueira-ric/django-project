from django.test import TestCase
from django.urls import reverse,resolve
from recipes import views
from recipes.models import Recipe, Category
from django.contrib.auth.models import User

class RecipeViewTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipe(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1> No Recipes found </h1>',
            response.content.decode('utf-8')
            )

    def test_recipe_load_template_loads_recipes(self):
        category = Category.objects.create(name='Category-test')
        author = User.objects.create_user(
            first_name = 'user',
            last_name = 'name',
            username = 'user1',
            password = '123455',
            email = 'user@user.com',
        )
        recipe = Recipe.objects.create(
            category = category,
            author = author,
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutes',
            servings = '4',
            servings_unit = 'people',
            preparation_steps = 'Recipe Preparation Steps',
            preparation_steps_is_html = False,
            is_published = True,
        ) 
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('Recipe Title', content) 

        response_recipes = response.context['recipes']
        self.assertEqual(response_recipes.first().title, 'Recipe Title')
        self.assertEqual(len(response.context['recipes']), 1)
        

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs=({'id':1})))
        self.assertIs(view.func, views.recipe)

    def test_recipe_category_view_return_404_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_return_404_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
            )
        self.assertEqual(response.status_code, 404)