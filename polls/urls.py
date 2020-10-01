from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    #path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
   # path('bootstrap/',TemplateView.as_view(template_name="boootstrap/test.html")),
    path('<int:pk>/vote/',views.vote,name='vote')
]