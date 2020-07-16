from django.shortcuts import render,HttpResponse
from background_task import background
# Create your views here.
import time
@background(schedule=1)
def task_hello():
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    print("task ... Hello World!", time_str)

import requests
from bs4 import BeautifulSoup
import sqlite3
@background(schedule=10)
def task_crawling_daum():
    res = requests.get('http://media.daum.net/economic/')
    links = []
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        links = soup.find_all('a', class_='link_txt')
        # conn = sqlite3.connect('economic.db')
        # conn.close()
        
        with sqlite3.connect("db.sqlite3") as con:
            # query = 'CREATE TABLE economic (title TEXT, link TEXT)'
            # con.execute(query)
            # con.commit()
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
