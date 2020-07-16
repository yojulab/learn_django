from django.shortcuts import render

# Create your views here.
def home(request):
    data = request.GET.copy()
    return render(request, 'home.html', context=data)

import sqlite3
def list(request):
    data = request.GET.copy()
    # rows_list = []
    with sqlite3.connect("db.sqlite3") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from economic")
        data['rows'] = cur.fetchall()
        # for row in rows:
        #     rows_list.append(dict(zip([c[0] for c in cur.description], row)))
    # data['rows'] = [{'title':'title01'},{'title':'title02'}]
    return render(request, 'list.html', context=data)
