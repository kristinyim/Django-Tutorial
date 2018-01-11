from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader
from .models import Question

# Create your views here.

#INDEX

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

# Second version with Templates but without render
# need loader import for this
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	# looks inside template folder for this
# 	template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list': latest_question_list,
# 	}
# 	return HttpResponse

# First simpliest verson without templates or render
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	output = ', '.join([q.question_text for q in latest_question_list])
# 	return HttpResponse(output)

# DETAIL

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})
# There's also get_list_or_404 which uses filter() instead of get()
# so it can raise a Http404 if the list is empty

# Second version w/404 but in a long windy way
# def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist")
# 	return render(request, 'polls/detail.html', {'question': question})

# First simpliest static html response
# def detail(request, question_id):
#	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)