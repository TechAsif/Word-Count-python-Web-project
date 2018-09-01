from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You ar at the polls index.")