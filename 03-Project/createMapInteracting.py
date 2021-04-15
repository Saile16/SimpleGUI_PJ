# instalamos folium
# pip install folium
import folium
import pandas as pd
# por ejemplo ahora si queremos usar valores de un archivo externo podemos usar pandas
# leemos el archivo y lo guuardamos en una variable data
data = pd.read_csv("Volcanoes.txt")
# aqui podemos obtener los valore de data de esta manera
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# de estamaera obtenemos la ubicacion o lo ue quermos ver
# el tiles= Stamen terrain es para cambiar el background
map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
# para crear coordenadas rapidamente en ves de escribir muchaslineas de codigo
# podemos pasar una lista en un loop for
# en este caso como lat y lon son listas separadas usamos zip para poder unirlas
for lt, ln, el, name in zip(lat, lon, elev, name):
    # fg.add_child(folium.Marker(location=[lt, ln], popup=str(
    #     el)+"m", icon=folium.Icon(color=color_producer(el))))
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=str(
        el)+" m", fill_color=color_producer(el), color="black", fill_opacity=0.7))

fg1 = folium.FeatureGroup(name="Population")
# agregamos multipolygons
fg1.add_child(folium.GeoJson(
    # si quisieramos cambiar el color dentro de los poligonos usamos stylefunction
    data=(open('world.json', 'r', encoding='utf-8-sig').read()),
    style_function=lambda x: {"fillColor": "green" if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())
# aqui guardamos y creamos el archivo html
map.save("Map1.html")
