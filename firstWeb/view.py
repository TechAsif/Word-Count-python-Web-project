from django.http import HttpResponse


def home(request):

	return HttpResponse('<h1>hellow</h1>')

def blog(request):

	return HttpResponse('<h1>This is blog page </h1>')