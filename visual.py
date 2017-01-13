import bokeh
#from bokeh.charts import Scatter, output_file, save
from numpy import *
import numpy as np
from bokeh.plotting import figure, output_file, save
import pandas as pd
co2 = pd.read_csv('CO2E.csv')
gdp = pd.read_csv('GDP.csv')

co2.fillna(0)
gdp.fillna(0)
#co2.transpose()

yvalue = []
xvalue = []
y2value = []

for yr in range(1970,2013):
    s = 0
    sg = 0
    co2[np.isnan(co2[str(yr)])] = 0
    gdp[np.isnan(gdp[str(yr)])] = 0
    for t in co2[str(yr)]:
        s += t
    for g in gdp[str(yr)]:
        sg += g
    yvalue.append(s)
    y2value.append(sg/1000000)
    xvalue.append(yr)

#p = Scatter(co2, x=xvalue, y=yvalue, title='Name')

p = figure(plot_width=1280, plot_height=720, title="CO2 Emission in Kilo-tons Global")

p.line(xvalue, yvalue, line_width=2, color="black", legend="CO2")

output_file("plot.html")

save(p)

q = figure(plot_width=1280, plot_height=720, title="CO2 Emission in Kilo-tons vs GDP in Millions USD Global")
q.line(xvalue, yvalue, line_width=2, color = "black", legend = "co2")
q.line(xvalue, y2value, line_width=2, color = "green", legend = "GDP")

output_file("plot2.html")

save(q)
