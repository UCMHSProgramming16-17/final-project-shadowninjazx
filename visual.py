import bokeh
#from bokeh.charts import Scatter, output_file, save
from numpy import *
import numpy as np
from bokeh.plotting import figure, output_file, save
import pandas as pd
co2 = pd.read_csv('CO2E.csv')
co2.fillna(0)
#co2.transpose()

yvalue = []
xvalue = []

for yr in range(1970,2013):
    s = 0
    co2[np.isnan(co2[str(yr)])] = 0
    for t in co2[str(yr)]:
        s += t
    yvalue.append(s)
    xvalue.append(yr)

#p = Scatter(co2, x=xvalue, y=yvalue, title='Name')

p = figure(plot_width=1280, plot_height=720, title="CO2 Emission in Kilo-tons")

p.line(xvalue, yvalue, line_width=2, color="black", legend="CO2")


output_file("plot.html")

save(p)


