# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello, Django!")

from django.shortcuts import render		# add
def home(request):
    return render(request, 'home.html')    

