import folium
import pandas
import random

map = folium.Map(location=[47.232157, 39.597106], zoom_start=6)
data = pandas.read_csv("files/data.csv")
lat = list(data["latitude_1"])
lon = list(data["longitude_1"])
elev = list(data["type_object"])

random_color = ['blue', 'green', 'black', 'gray', 'orange', 'red', 'pink',
                'purple', 'purple', 'darkgreen', 'lightred', 'cadetblue']

fgv = folium.FeatureGroup(name="Markers")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=7, fill_color=random.choice(random_color),
                                     popup=el, fill_opacity=0.7, color='None', fill=True))


fgp = folium.FeatureGroup(name="Population")

map.add_child(folium.GeoJson(data=open("files/world.json", 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: dict(fillColor='green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'lightred')))


map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("files/Map1.html")
