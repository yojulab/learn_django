from django.shortcuts import render,HttpResponse
from background_task import background
# Create your views here.
@background(schedule=1)
def task_hello():
    print("task ... Hello World!")

import requests
from bs4 import BeautifulSoup
@background(schedule=10)
def task_crawling_daum(repeat=100):
    res = requests.get('http://media.daum.net/economic/')
    links = []
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        links = soup.select('a[href]')
    print('task_crawling_daum : ', type(links), len(links))