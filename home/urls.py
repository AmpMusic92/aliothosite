from django.urls import path
#non ha senso mettere gli url all'interno delle apps!
from . import views
from django.views.generic import TemplateView
#remember to include the name of the app while reversing home:redirect
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
  #  path('done/redirect', views.redirect, name='redirect')
    #path('', TemplateView.as_view( template_name="boootstrap/test.html" )),
    #path('<int:menu_id>', views.redirect,name='redirect')

   ]