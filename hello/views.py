# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello, Django!")
def home(request):
    return HttpResponse("Hello, Django!")

from django.shortcuts import render		# add
def responsewithhtml(request):
    # data = {'first': 'Sanghun', 'second': 'Oh'}						# add
    data = dict()
    data['first'] = request.GET['first']
    data['second'] = request.GET['second']
    return render(request, 'hello/responsewithhtml.html', context=data)

def form(request):							# add
    return render(request, 'hello/requestform.html')    

def requestwithservice(request):
   data = request.GET.copy()        
   data['result'] = cal(data['firstvalue'], data['secondvalue'])
   return render(request, 'hello/requestwithservice.html', context=data)
   
def cal(first, second):
   result = int(first) * int(second)
   return result

def template(request):	
   return render(request, 'hello/template.html')
