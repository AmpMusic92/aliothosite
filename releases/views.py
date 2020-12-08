from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Release
# Create your views here.

def index(request):

    listOfReleases= Release.objects.all().order_by('-releaseDate')
    template = loader.get_template('releases/index.html')
    context = {
        'releases': listOfReleases
}

    return HttpResponse( template.render( context, request ) )
