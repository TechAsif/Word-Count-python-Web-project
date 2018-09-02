from django.http import HttpResponse
from django.shortcuts import render


def home(request):

	return render(request,'index.html')

def count(request):

	fullname = request.GET['fullname']
	print(fullname)
	return render(request,'count.html',{'fullname':fullname})