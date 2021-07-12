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