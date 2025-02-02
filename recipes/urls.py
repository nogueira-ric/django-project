### To better manage Django files, it is advisable to create a URLS.py file inside the app to work with. 
# That way you can include these files in the urls.py file at the root of the project. 
# It helps to make the code more cohesive. 

from django.urls import path
#Must import views from app recipes
from recipes.views import home, about, contact


urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact', contact)
]