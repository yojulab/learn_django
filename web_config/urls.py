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
from django.urls import path, include

from hello import views	as helloview
from homes import views	as homesview
from maps import views	as mapsview
from polls import views as pollsview
from livestream import views as livestreamview
from members import views as membersview

urlpatterns = [
    path('admin/', admin.site.urls),

    path("hello", helloview.hello, name="hello_home"),
    path('home', helloview.home),

    path('', homesview.index, name='index'),
    path('homes/', include('homes.urls')),
    path('boards/', include('boards.urls')),

    path('maps/showmapwithfolium', mapsview.showmapwithfolium, name='show_map'),
    path('maps/showchartwithplotly', mapsview.showchartwithplotly, name='show_plotly'),

    path('polls/index', pollsview.index, name='polls_index'),

    path('livestreamview/livestreamwithcv2', livestreamview.livestreamwithcv2, name='livestreamwithcv2'),

    path('members/loginform', membersview.login_form, name='membersview.login_form'),
    path('members/login', membersview.login, name='membersview.login'),
    path('members/logout', membersview.logout, name='membersview.logout'),
]
