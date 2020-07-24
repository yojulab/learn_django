from django.shortcuts import render,HttpResponse
from background_task import background
# Create your views here.
import time
@background
def task_hello(schedule=3, repeat=10):
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    print("task ... Hello World!", time_str)


import requests
from bs4 import BeautifulSoup
import sqlite3
@background
def task_crawling_daum(schedule=60, repeat=60*60*1):
    res = requests.get('http://media.daum.net/economic/')
    links = []
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        links = soup.find_all('a', class_='link_txt')
        # conn = sqlite3.connect('db.sqlite3')
        # query = 'CREATE TABLE economic (title TEXT, link TEXT)'
        # conn.execute(query)
        # conn.commit()
        # conn.close()
        
        with sqlite3.connect("db.sqlite3") as con:
            cur = con.cursor()
            title = ''
            link = ''
            query = "INSERT INTO economic (title,link) VALUES (?,?)"
            for link in links:
                title = str.strip(link.get_text())
                link = link.get('href')
                cur.execute(query,(title,link))
            con.commit()
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    print('task_crawling_daum : ', type(links), len(links), time_str)