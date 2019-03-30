print('hello,github!')
from django.shortcuts import redirect 
from django.http import HttpResponse

def index(request):
	return HttpResponse('index')

def login(request):
	return redirect('/index')
