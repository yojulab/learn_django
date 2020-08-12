from hello import views	
from django.urls import path			# add
urlpatterns = [
    path("", views.main, name="main"),
    path("home", views.home, name="home"),
    path("form/", views.form, name="form"),
    path("template/", views.template, name="template"),
    path("templatefromsite/", views.templatefromsite, name="template"),
]
