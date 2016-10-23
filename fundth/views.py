
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Question
from django.template import Context, loader
from django.views.generic import TemplateView

def index(request):
	context = {'jason_is_dumb': True}
	return render(request, 'fundth/index.html', context)

def organizationLogin(request):
	return render(request, 'fundth/organizationLogin.html')

def businessLogin(request):
	return render(request, 'fundth/businessLogin.html')

def businessNewAccount(request):
	return render(request, 'fundth/businessNewAccount.html')

def organizationNewAccount(request):
	return render(request, 'fundth/organizationNewAccount.html')


