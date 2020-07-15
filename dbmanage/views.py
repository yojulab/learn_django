from django.shortcuts import render

# Create your views here.
def home(request):
    data = request.GET.copy()
    return render(request, 'home.html', context=data)

def list(request):
    data = request.GET.copy()
    with sqlite3.connect("economic.db") as con:
        cur = con.cursor()
        cur.execute("select * from economic")
        data['rows'] = cur.fetchall()
    return render(request, 'list.html', context=data)
