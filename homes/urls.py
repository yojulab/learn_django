from django.urls import path
from . import views

urlpatterns = [
    path("responsewithhtml/", views.responsewithhtml),
    path("requestform/", views.requestform, name="homes_requestform"),		# add
    path("responsewithservice/", views.responsewithservice),
    path("template/", views.template, name="template"),				# add
    path("responsedeeplearning/", views.response_deeplearning, name="responsedeeplearning"),				# add
]