from django.shortcuts import render,HttpResponse
from background_task import background
# Create your views here.
@background(schedule=1)
def task_hello():
    print("task ... Hello World!")

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
        conn = sqlite3.connect('economic.db')
        conn.execute('CREATE TABLE economic (title TEXT, link TEXT)')
        conn.close()
        query = "INSERT INTO economic (title,link) VALUES (?,?)"
        with sqlite3.connect("economic.db") as con:
            cur = con.cursor()
            title = ''
            link = ''
            for link in links:
                title = str.strip(link.get_text())
                link = link.get('href')
                cur.execute(query,(title,link)); 
            con.commit();
    print('task_crawling_daum : ', type(links), len(links))