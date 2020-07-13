from hello import views	
from django.urls import path			# add
urlpatterns = [
    path("", views.home, name="home"),
    path("form/", views.form, name="form"),
]
