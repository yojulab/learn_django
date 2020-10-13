# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello, Django!")
def home(request):
    return render(request, 'home.html')    

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

# http://localhost:8000/hello/responsedeeplearning/?x1=0&x2=1
def response_deeplearning(request):
   data = request.GET.copy()        
   data['result'] = XORwithKeras(data['x1'], data['x2'])	# Modify
   return render(request, 'hello/response_deeplearning.html', context=data)

import tensorflow as tf
def XORwithKeras(x1, x2):
   new_model = tf.keras.models.load_model('datas/XORwithKeras.h5')
   param = [int(x1), int(x2)]
   result = new_model.predict([param])
   return result 
