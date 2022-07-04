from django.urls import path
from . import views

urlpatterns = [
    path("listwithrawquery/", views.listwithrawquery, name="listwithrawquery"),				# add
    path("listwithrawquerywithpaginator/", views.listwithrawquerywithpaginator, name="listwithrawquerywithpaginator"),				# add
    path("listwithmongo/", views.listwithmongo, name="listwithmongo"),				# add
    path("listwithmongowithpaginator/", views.listwithmongowithpaginator, name="listwithmongowithpaginator"),				# add
]