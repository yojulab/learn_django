from django.shortcuts import render

def index(request):
    return render(request, 'index.html')    

def responsewithhtml(request):
    data = {'first': 'Sanghun', 'second': 'Oh'}						# add
    data = dict()
    data['first'] = request.GET['first']
    data['second'] = request.GET['second']
    return render(request, 'homes/responsewithhtml.html', context=data)

def requestform(request):							# add
    return render(request, 'homes/requestform.html')    

def responsewithservice(request):
   data = request.GET.copy()        
   data['result'] = cal(data['firstvalue'], data['secondvalue'])
   return render(request, 'homes/responsewithservice.html', context=data)
   
def cal(first, second):
   result = int(first) * int(second)
   return result


# Create your views here.
def template(request):	
   return render(request, 'homes/template.html')

# http://localhost:8000/homes/responsedeeplearning/?x1=0&x2=1
def response_deeplearning(request):
   data = request.GET.copy()        
   data['result'] = XORwithKeras(data['x1'], data['x2'])	# Modify
   return render(request, 'homes/response_deeplearning.html', context=data)

import tensorflow as tf
def XORwithKeras(x1, x2):
   new_model = tf.keras.models.load_model('datas/XORwithKeras.h5')
   param = [int(x1), int(x2)]
   result = new_model.predict([param])
   return result 
