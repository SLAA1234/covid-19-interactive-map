# making a table, as variable
def findTopDeathsCases(x):
    import pandas as pd;
    df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/06-11-2020.csv');
    df_country = df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active', 'Lat', 'Long_']];
    df_Deaths = df_country.sort_values(['Deaths'], ascending=False);
    topDeaths = df_Deaths.head(x)
    return topDeaths;

topDeaths = findTopDeathsCases(15).to_html();

# make a map
import folium;
import pandas as pd;
df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/06-11-2020.csv');
m = folium.Map(location = [55.5999619,13.0059402],
            tiles = 'Stamen Terrain',
            zoom_start = 6);
def marker(x):
    folium.Marker(location=[x[0], x[1]],
                tooltip="Click for more",
                popup='{}\nConfirmed Cases: {}'.format(x[3],x[2]),
                icon=folium.Icon(color='black'),
                control_scale=True
                ).add_to(m);
df[['Lat', 'Long_', 'Confirmed','Combined_Key']].dropna(subset=['Lat','Long_']).apply(lambda x: marker(x), axis=1);

html_map = m._repr_html_(); 

from pip._internal.commands import debug

from flask import Flask, render_template;

app = Flask(__name__)

# show with table     return render_template('home.html', table=topDeaths, cmap=html_map);


@app.route('/')
def home():
    return render_template('home.html', cmap=html_map);

if __name__ == '__main__':
    app.run(debug==True);
