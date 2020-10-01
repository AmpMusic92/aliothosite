from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuField,Title
from django.template import loader
from django.shortcuts import redirect

# Create your views here.
def index(request):
    menuFields = MenuField.objects.all()
    title = Title.objects.all()[0]
    template = loader.get_template( 'home/index.html' )
    context = {
        'menuFields': menuFields,
        'title': title
    }
    return HttpResponse( template.render( context, request ) )

def redirect(request):
    response = redirect("http://www.google.com")
    return response



