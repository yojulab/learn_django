from django.shortcuts import render

# Create your views here.
from django.db import connection
import sqlite3

def listwithrawquery(request):
    data = request.GET.copy()
    # data = dict()
    # connection.row_factory = sqlite3.Row
    # cursor = connection.cursor()
    with sqlite3.connect("db.sqlite3") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor();	cur.execute("select * from economic")
        data['rows'] = cur.fetchall()

    for row in data['rows']:
        print(f"{row['title']}, {row['link']}")

    return render(request, 'board/listwithrawquery.html', context=data)

from django.core.paginator import Paginator
def listwithrawquerywithpaginator(request):
    data = request.GET.copy()
    # data = dict()
    # connection.row_factory = sqlite3.Row
    # cursor = connection.cursor()
    with sqlite3.connect("db.sqlite3") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor();	cur.execute("select * from economic")
        contact_list = cur.fetchall()

    paginator = Paginator(contact_list, 5) # Show 15 contacts per page.

    page_number = request.GET.get('page')
    page_number = page_number if page_number else 1 
    data['page_obj'] = paginator.get_page(page_number)

    page_obj=data['page_obj']
    for row in page_obj:
        print(f"{row['title']}, {row['link']}")

    return render(request, 'board/listwithrawquerywithpaginator.html', context=data)

from pymongo import MongoClient
from board.mongopaginator import MongoPaginator
def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://10.0.0.5:27017/')  as client:
        mydb = client.mydb
        result = list(mydb.economic.find({}))			# get Collection with find()
        
        result_page = []
        for info in result:						# Cursor
            # del info(_id)
            temp = {'title':info['title'], 'link':info['link']}
            result_page.append(temp)
            print(type(info), info)
        data['page_obj'] = result
        
    return render(request, 'board/listwithmongo.html', context=data)

def listwithmongowithpaginator(request):
    data = request.GET.copy()
    with MongoClient('mongodb://192.168.0.6:27017/')  as client:
        mydb = client.mydb
        contact_list = mydb.economic.find({})			# get Collection with find()
        for info in contact_list:						# Cursor
            print(info)

    paginator = MongoPaginator(contact_list, 5) # Show 15 contacts per page.

    page_number = request.GET.get('page', 1)
    data['page_obj'] = paginator.get_page(page_number)

    page_obj=data['page_obj']
    for row in page_obj:
        print(f"{row['title']}, {row['link']}")

    return render(request, 'board/listwithrawquerywithpaginator.html', context=data)
