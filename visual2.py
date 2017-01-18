import bokeh
from numpy import *
import numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.charts import Scatter, output_file, save
import pandas as pd
#Impory modules

co2 = pd.read_csv('co2re.csv')
gdp = pd.read_csv('gdpre.csv')
#Read csv files using pandas and save as dataframe


output_file("plot4.html")
#Set output file

p = figure(plot_width=1920, plot_height=1080, title="CO2 Emmission of Countries")
#Initate plot

p.line(co2['Year'], co2['China'], line_width=2, color = "red", legend = "China")
p.line(co2['Year'], co2['United States'], line_width=2, color = "blue", legend = "United States")
p.line(co2['Year'], co2['Japan'], line_width=2, color = "purple", legend = "Japan")
p.line(co2['Year'], co2['Germany'], line_width=2, color="black", legend = "Germany")
#Defien lines for co2 values of china, us, japan, and germany

save(p)
#Save plot

output_file("plot5.html")
#Set output file

q = figure(plot_width=1920, plot_height=1080, title="GDP of Countries")
#Initiate plot

q.line(gdp['Year'], gdp['China'], line_width=2, color = "red", legend = "China")
q.line(gdp['Year'], gdp['United States'], line_width=2, color = "blue", legend = "United States")
q.line(gdp['Year'], gdp['Japan'], line_width=2, color = "purple", legend = "Japan")
q.line(gdp['Year'], gdp['Germany'], line_width=2, color="black", legend = "Germany")
#Define lines for co2 values of china, us, japan, and germany

save(q)
#Save plot