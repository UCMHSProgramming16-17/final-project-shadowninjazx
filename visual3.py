from bokeh.charts import Area, save, output_file, defaults
import pandas as pd
import numpy as np
#Import libraries

defaults.width = 1280   
defaults.height = 720
#Set graph width and height

co2 = pd.read_csv('co2re.csv')
#read csv file

co2 = co2.fillna(0)
#fill na as zero

co2 = co2[co2.China != 0]
#delete rows where there are values of zero

cols = ['China', 'United States','Japan']
#Select a list of countries

co2[cols] = co2[cols].applymap(np.int64)
#convert floats to integers

data = dict(
    china=co2['China'],
    usa=co2['United States'],
    japan=co2['Japan'],
)
#Define a dictionary with elements from co2 and countries of china, us, and japan

area1 = Area(data, title="Stacked Area Chart of CO2 Emmission", legend="top_left",
             stack=True, xlabel='Year Since 1960', ylabel='Kilo-ton CO2')
#Define stacked area chart

output_file("area.html")
#Set output file

save(area1)
#Save graph

gdp = pd.read_csv('gdpr.csv')
#Read csv with pandas

gdp = gdp[gdp.China != 0]
#Delete rows with 0 values

gdp[cols] = gdp[cols].applymap(np.int64)
#Make floats integers

data2 = dict(
    china=gdp['China'],
    usa=gdp['United States'],
    japan=gdp['Japan'],
)
#Define dictionary to store three columns of gdp data

area2 = Area(data2, title="Stacked Area Chart of GDP", legend="top_left",
             stack=True, xlabel='Year Since 1960', ylabel='Million USD')
#define stacked area graph for gdp

output_file('area2.html')
#set new output file

save(area2)
#save new graph