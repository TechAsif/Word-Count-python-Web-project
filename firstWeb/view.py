from django.http import HttpResponse
from django.shortcuts import render


def home(request):

	return render(request,'index.html')

def blog(request):

	return HttpResponse('<h1>This is blog page </h1>')