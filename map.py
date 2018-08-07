import folium

wmap = folium.Map(location=[43.832248, -79.309740], zoom_start=10, tiles = "Mapbox Bright")
wmap.add_child(folium.Marker(location=[43.835193, -79.307205], popup = "Amarillo Campus", 
                             icon = folium.Icon(color = "blue")))
wmap.add_child(folium.Marker(location=[43.832248, -79.309740], popup = "Main Campus", 
                        icon = folium.Icon(color = "purple")))
wmap.add_child(folium.Marker(location = [43.828240, -79.308264], popup = "Milliken Campus", 
                             icon = folium.Icon(color = "red")))
wmap.save("Map1.html")
