from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template

# Create your views here.
def home(request):
    # return HttpResponse("Hello, Django!")
    # data = {'first': 'Sanghun', 'second': 'Oh'}
    data = request.GET.copy()         # ?first=Sanghun&second=Oh
    print(data)
    data['result'] = cal(data['first'], data['second'])
    return render(request, 'hello/home.html', context=data)

def form(request):
    data = request.GET.copy() 
    return render(request, 'hello/form.html', context=data)

def cal(first, second):
    result = int(first) * int(second)
    return result