"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", include("hello.urls")),
    path("dbmanage/", include("dbmanage.urls")),
    # path("crawling/", include("crawling.urls")),
]

from crawling.crawling_tasks import task_hello, task_crawling_daum		# add
task_hello(schedule=20, repeat=59*59*24)
task_crawling_daum(schedule=10, repeat=59*59*24)
# task_hello(schedule=20, repeat=60*4)
# task_crawling_daum(schedule=10, repeat=59*3)