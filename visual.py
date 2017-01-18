import bokeh
from bokeh.charts import Scatter, output_file, save
from numpy import *
import numpy as np
from bokeh.plotting import figure, output_file, save
import pandas as pd
#Import Modules

co2 = pd.read_csv('CO2E.csv')
gdp = pd.read_csv('GDP.csv')
#Load Pandas Dataframe from csv files

yvalue = []
xvalue = []
y2value = []
#Initiate empty list

for yr in range(1970,2013):
#For loop to find sum of year
    s = 0
    sg = 0
    #Set initial temporary sums to zero
    co2[np.isnan(co2[str(yr)])] = 0
    #Set NA values to zero
    gdp[np.isnan(gdp[str(yr)])] = 0
    #Set NA values to zero
    
    for t in co2[str(yr)]:
    #For loop for every element in co2
        s += t
        #Sum up 
        
    for g in gdp[str(yr)]:
    #For loop for every element in gdp
        sg += g
        #Sum up gdp
        
    yvalue.append(s/2)
    #Add sum per year to list divide by two because there is a world row that recounts the total
    y2value.append(sg/2000000)
    #Add sum per year to list divide by two million because units is in 1 million and there is a world row that recounts the total
    xvalue.append(yr)
    #Append year for x values


p = figure(plot_width=1280, plot_height=720, title="CO2 Emission in Kilo-tons Global")
#Initiate plot

p.line(xvalue, yvalue, line_width=2, color="black", legend="CO2")
#Define line for CO2

output_file("plot.html")
#Set output file

save(p)
#Save grpah

q = figure(plot_width=1280, plot_height=720, title="CO2 Emission in Kilo-tons vs GDP in Millions USD Global")
#Initiate plot

q.line(xvalue, yvalue, line_width=2, color = "black", legend = "co2")
q.line(xvalue, y2value, line_width=2, color = "green", legend = "GDP")
#Set GDP and CO2 lines

output_file("plot2.html")
#Set output file

save(q)
#Save graph

df = {'CO2':yvalue,'GDP':y2value}
#Initiate new datafram with only co2 and gdp values

r = Scatter(df, x = 'CO2', y = 'GDP', title = "GDP vs CO2", xlabel = "CO2 in Kilo-tons", ylabel = "GDP in Millions USD")
#Create scatter graph

output_file("plot3.html")
#Set output file

save(r)
#Save graph