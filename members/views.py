from django.shortcuts import render

# Create your views here.


def login_form(request):
    data = request.GET.copy()
    return render(request, 'members/login_form.html', context=data)

from django.contrib.auth import authenticate
from django.db import connection
import sqlite3
def login(request):
    data = request.POST.copy()
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        data['user'] = user
        print('get authenticate!')
        # connection.row_factory = sqlite3.Row
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM auth_user WHERE username = %s", [username])
            row = cursor.fetchone()
    else:
        # No backend authenticated the credentials
        print('cant get authenticate!')
    return render(request, 'members/login_out.html', context=data)

from django.contrib.auth import logout
def logout(request):
    data = request.GET.copy()
    # logout(request)
    return render(request, 'members/login_out.html', context=data)
