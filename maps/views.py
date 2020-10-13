chfrom django.shortcuts import render

# Create your views here.
import folium
def showmapwithfolium(request):  
    #creation of map comes here + business logic
    Lat_long = [35.3369, 127.7306]
    maps = folium.Map(Lat_long, zoom_start=10)
    popText = folium.Html('<b>Jirisan</b></br>'+str(Lat_long), script=True)
    popup = folium.Popup(popText, max_width=2650)
    folium.RegularPolygonMarker(location=Lat_long, popup=popup).add_to(maps)
    maps=maps._repr_html_() #updated
    datas = {'mountain_map': maps}

    return render(request, 'maps/showmapwithfolium.html', context=datas)