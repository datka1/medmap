import folium
from folium.plugins import MarkerCluster
from folium.plugins import LocateControl
import json

m = folium.Map(location=[41.69342, 44.80182], zoom_start=11)
mk = MarkerCluster().add_to(m)
lc = LocateControl().add_to(m)

node = json.load(open('pharmacy_geo.geojson', encoding='utf8'))
gj = folium.GeoJson(node)

try:
    for feature in gj.data['features']:
        if feature['geometry']['type'] == 'Point':
            folium.Marker(location=list(reversed(feature['geometry']['coordinates'])),                     
                          popup=folium.Popup(feature['properties']['name'])
                            ).add_to(mk)
    
except:
    pass
    
m.save('index.html')    