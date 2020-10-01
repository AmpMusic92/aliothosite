from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')

def detail (request,question_id):
    question = Question.objects.get(id=question_id)
    template = loader.get_template('polls/detail.html')
    context = {
        'question':question

    }

    return HttpResponse(template.render(context,request))

def results (request,question_id):
    response = "Your are looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote (request,question_id):
    return HttpResponse("You're voting on question %s"  % question_id)