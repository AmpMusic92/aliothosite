from django.urls import path

from . import views
from django.views.generic import TemplateView
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    #path('', TemplateView.as_view( template_name="boootstrap/test.html" )),
    #path('<int:menu_id>', views.redirect,name='redirect')

   ]