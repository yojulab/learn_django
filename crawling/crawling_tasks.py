from django.shortcuts import render,HttpResponse
from background_task import background
# Create your views here.
@background(schedule=1)
def task_hello():
    print("task ... Hello World!")

@background(schedule=)
def task_hello():
    print("task ... Hello World!")    