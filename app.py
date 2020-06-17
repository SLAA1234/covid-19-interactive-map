import folium;
import ipywidgets;
import pandas as pd;
from folium import plugins;
from pip._internal.commands import debug
from flask import Flask, render_template;

# import data
df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/06-16-2020.csv');

# map. use Malmö' location as center
m = folium.Map(location = [55.5999619,13.0059402], zoom_start=6)

#show map types using ipywidgets     
select_widget=ipywidgets.Select(
    options=['Open Street Map', 'Stamen Terrain', 'Toner', 'Watercolor', 'Positron', 'Dark Matter'],
        value='Stamen Terrain',
        description='Map Type:',
        disabled=False)
           
def select(map_type):
    if map_type == 'Stamen Terrain':
        return folium.Map(location = [55.5999619,13.0059402],
            tiles = 'Stamen Terrain',
            zoom_start = 6);
    if map_type == 'Open Street Map':
        return folium.Map(location = [55.5999619,13.0059402],
            tiles = 'Open Street Map',
            zoom_start = 6);
    if map_type == 'Toner':
        return folium.Map(location = [55.5999619,13.0059402],
            tiles = 'Stamen Toner',
            zoom_start = 6);
    if map_type == 'Watercolor':
        return folium.Map(location = [55.5999619,13.0059402],
            tiles = 'Stamen Watercolor',
            zoom_start = 6);
    if map_type == 'Positron':
        return folium.Map(location = [55.5999619,13.0059402],
            tiles = 'CartoDB Positron',
            zoom_start = 6);
    if map_type == 'Dark Matter':
        return folium.Map(location = [55.5999619,13.0059402],
            tiles = 'CartoDB Dark_Matter',
            zoom_start = 6);  
           
  
ipywidgets.interact(select, map_type=select_widget)
    
# add layer control to show different maps
# add tiles to map
folium.raster_layers.TileLayer('Open Street Map').add_to(m)
folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)
        
folium.LayerControl().add_to(m)

# add mini map to map
minimap = plugins.MiniMap(location = [55.5999619,13.0059402],toggle_display=True)
m.add_child(minimap)

# add scroll zoom toggler to map
plugins.ScrollZoomToggler().add_to(m)

# add full screen button to map
plugins.Fullscreen(position='topright').add_to(m)

# add marker. Large data so use apply instead of for-loop
def marker(x):
    folium.Marker(location=[x[0], x[1]],
                tooltip="Click for more",
                popup='{}\n<strong>Confirmed</strong>: {}\n <strong>Deaths</strong>: {}'.format(x[3],x[2], x[4]),
                icon=folium.Icon(color='black'),
                control_scale=True
                ).add_to(m);
df[['Lat', 'Long_', 'Confirmed','Combined_Key', 'Deaths']].dropna(subset=['Lat','Long_']).apply(lambda x: marker(x), axis=1);

# create html_map variable
html_map = m._repr_html_(); 

# import flask


app = Flask(__name__)

# show with table     return render_template('home.html', table=topDeaths, cmap=html_map);


@app.route('/')
def home():
    return render_template('home.html', cmap=html_map);

if __name__ == '__main__':
    app.run(debug==True);
