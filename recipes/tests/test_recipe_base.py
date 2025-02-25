from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        self.make_recipe()
        return super().setUp()
    
    def make_category(self, name = 'Category-test'):
        return Category.objects.create(name=name)
    
    def make_author(
            self,
            first_name = 'user',
            last_name = 'name',
            username = 'user1',
            password = '123455',
            email = 'user@user.com',
                    ):
        return User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email = email,
        )
    
    def make_recipe(
            self,
            category_data = None,
            author_data = None,
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
        ):

        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category = self.make_category(**category_data), ## In case of the category_data is None then unpack a dictionary to add new category
            author = self.make_author(**author_data),
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = False,
            is_published = True,
        )
4   