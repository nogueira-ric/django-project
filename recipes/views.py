from django.shortcuts import render
# Create your views here.

def home(request):
    #Rendering web applications. 
    #recipes/ points to the path of the templates, such as /recipes or global/.
    #This allows you to reuse files with the same name by simply pointing to the template path.
    return render(request,'recipes/home.html', context={
        'name': 'Ricardo Nogueira'
    })

