from django.shortcuts import render
from django.http import HttpResponse
from crawling.crawling_tasks import task_crawling_daum

# Create your views here.
def crawling_daum(request):
    # data = request.GET.copy()
    task_crawling_daum()
    return HttpResponse("complate crawling from daum economic!")
