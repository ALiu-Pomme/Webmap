import folium

wmap = folium.Map(location=[43.832248, -79.309740], zoom_start=10, tiles = "Mapbox Bright")

fg = folium.FeatureGroup(name = "My Map")

for coordinates in [[43.835193, -79.307205], [43.832248, -79.309740], [43.828240, -79.308264]]:
    fg.add_child(folium.Marker(location=coordinates, popup = "Campus Location", 
                             icon = folium.Icon(color = "blue")))

wmap.add_child(fg)
wmap.save("Map1.html")
