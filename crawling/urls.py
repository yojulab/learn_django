from crawling import views	
from django.urls import path			# add
urlpatterns = [
    path("crawling_daum/", views.crawling_daum, name=""),
]
