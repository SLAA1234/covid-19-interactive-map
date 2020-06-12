import pandas as pd;
import geopandas as gpd;
import re;
import requests;

# total case
url = 'https://www.worldometers.info/coronavirus/';

html_source = requests.get(url).text
html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source)

dataframe=pd.read_html(html_source)
print(dataframe)


