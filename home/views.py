from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuField,Title
from releases.models import Release
from django.template import loader
from django.shortcuts import redirect


# Create your views here.
def index(request):
    menuFields = MenuField.objects.all()
    title = Title.objects.all()[0]
    releaseText = Release.objects.all().order_by('-releaseDate')[0].releaseDesc
    releaseArtwork = Release.objects.all().order_by( '-releaseDate' )[0].imageLink

    template = loader.get_template( 'home/index.html' )
    context = {

        'menuFields': menuFields,
        'title': title,
        'releaseText':releaseText,
        'imageLink':releaseArtwork

    }
    return HttpResponse( template.render( context, request ) )

def redirect(request):
    response = redirect("http://www.google.com")
    return response



