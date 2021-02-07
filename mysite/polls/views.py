from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # '-' means the reversed order (descending order)
    # template = loader.get_template('polls/index.html')  # we got template shortcut
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request)) # we got template shortcut
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # # >>>>>> we got 404 short cut >>>>>>
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exit')
    # return render(request, 'polls/detail.html', {'question': question})
    # # <<<<<< we got 404 short cut <<<<<<

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question - {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question - {question_id}")
