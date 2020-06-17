# covid-19-interactive-map

Lisa Wang



This repository shows covid-19 data of 6/16/2020 on world map. Code was written in Python in Visual Studio Code.

<strong>Data</strong>:
Data comes from the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University./n
https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/06-16-2020.csv. 

<strong>Module</strong>:
folium is used to create map, control layer and add marker. Use Malmö as center of the map.
pandas is used to handle csv file and analyze data.
ipywidgets is used to show different map_type.
plugins is used to add minimap, ScrollZoomToggler and Full screen button to basic map.
flask is used to build a web application.

<strong>Class</strong>:
MapType is created.

<strong>Run</strong>:
run app.py in Visual Studio Code and then open http://localhost:5000/. 
