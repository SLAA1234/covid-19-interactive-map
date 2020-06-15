# import folium;
# import pandas as pd;
# import re;
# import requests;

# # total case
# url = 'https://www.worldometers.info/coronavirus/';

# html_source = requests.get(url).text;
# html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source);

# # type(data) return a list
# data=pd.read_html(html_source);

# # save data to dataframe. type(data_cases): <class 'pandas.core.frame.DataFrame'>
# # select only country and total cases
# for data_cases in data:
#     data_cases = data_cases[['Country,Other', 'TotalCases', 'TotalDeaths', 'TotalRecovered']];
#     print(data_cases)

# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello Lisa! Don\'t be too lazy!'


# if __name__ == '__main__':
#     app.run()

# from IPython.display import IFrame
# IFrame(src = 'https://coronavirus.jhu.edu/map.html', width = 1000, height = 600)

# def ihtml(self, line, cell):
#         height = int(line or 400)
#         url = "https://coronavirus.jhu.edu/map.html," + base64.b64encode(self.var_re.sub(self.var_replace, cell).encode('utf-8')).decode('utf-8')
#         display_html(IFrame(url, "100%", height)) 

import pandas as pd;
import folium;

# open csv
df = pd.read_csv('06-11-2020.csv');

# select columns. Group by country 
df = df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']];

# rank data
df = df.sort_values(['Deaths'], ascending=False);

# change column order
cols = df.columns.tolist();
df = df[[cols[1]] + [cols[0]] + cols[2:]];

# making a map
world_map = folium.Map()
world_map

# home.html
# <div class="container">
#     <div class = "row">
#         <div class=".col-1">{{ table | safe }}</div>
#         <div class=".col-11">{{ cmap | safe }}</div>
#     </div>
# </div>