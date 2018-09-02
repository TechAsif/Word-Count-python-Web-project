from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):

	return render(request,'index.html')

def count(request):

	fullname = request.GET['fullname']

	worldlist = fullname.split();

	worddictionary = {}

	for word in worldlist:
		if word in worddictionary:
			#increase
			worddictionary[word] +=1
		else:
			#add to the dictionary
			worddictionary[word]=1

	sortedword = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)		

	return render(request,'count.html',{'fullname':fullname,'count':len(worldlist),'worddictionarys':sortedword})



def about(request):
	return render(request,'about.html')