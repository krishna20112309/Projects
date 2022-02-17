import geocoder
import folium
g=geocoder.ip("122.161.53.30")

myAddress=g.latlng
print(myAddress)
my_map=folium.Map(location=myAddress,zoom_start=12)
folium.CircleMarker(location=myAddress,radius=50,popup="Delhi").add_to(my_map)
folium.Marker(myAddress,popup="Delhi").add_to(my_map)
my_map.save("my_map.html ")
