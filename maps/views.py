from django.shortcuts import render

# Create your views here.
import folium
def showmapwithfolium(request):  
    #creation of map comes here + business logic
    lat_long = [35.3369, 127.7306]
    m = folium.Map(lat_long, zoom_start=10)
    popText = folium.Html('<b>Jirisan</b></br>'+str(lat_long), script=True)
    popup = folium.Popup(popText, max_width=2650)
    folium.RegularPolygonMarker(location=lat_long, popup=popup).add_to(m)
    m=m._repr_html_() #updated
    datas = {'mountain_map': m}

    return render(request, 'maps/showmapwithfolium.html', context=datas)

def showchartwithplotly(request):
    # for bar plot
    xArray = ["Italy", "France", "Spain", "USA", "Argentina"]
    yArray = [55, 49, 44, 24, 15]
    result = {'xArray':xArray, 'yArray':yArray}


    # for multi plot
    x1Values = list(range(1,11))
    result['x1Values'] = x1Values
    y1Values = list(map(lambda x:x, x1Values))
    result['y1Values'] = y1Values
    y2Values = list(map(lambda x:1.5*x, x1Values))
    result['y2Values'] = y2Values
    y3Values = list(map(lambda x:1.5*x+7, x1Values))
    result['y3Values'] = y3Values

    return render(request, 'maps/showchartwithplotly.html', context=result)
