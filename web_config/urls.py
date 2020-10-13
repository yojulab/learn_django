"""web_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from hello import views	as helloview
from board import views	as boardview
from maps import views	as mapsview
urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello", helloview.hello, name="hello_home"),
    path('', helloview.home, name='home'),
    path('home', helloview.home),
    path("hello/responsewithhtml/", helloview.responsewithhtml),
    path("hello/form/", helloview.form, name="helloform"),		# add
    path("hello/requestwithservice/", helloview.requestwithservice),
    path("hello/template/", helloview.template, name="template"),				# add
    path("hello/responsedeeplearning/", helloview.response_deeplearning, name="responsedeeplearning"),				# add

    path("board/listwithrawquery/", boardview.listwithrawquery, name="listwithrawquery"),				# add
    path("board/listwithrawquerywithpaginator/", boardview.listwithrawquerywithpaginator, name="listwithrawquerywithpaginator"),				# add
    path("board/listwithmongo/", boardview.listwithmongo, name="listwithmongo"),				# add
    path("board/listwithmongowithpaginator/", boardview.listwithmongowithpaginator, name="listwithmongowithpaginator"),				# add

    path('maps/showmapwithfolium', mapsview.showmapwithfolium, name='show_map'),
]
