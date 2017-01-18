import pandas as pd
co2 = pd.read_csv('CO2E.csv')
gdp = pd.read_csv('GDP.csv')

#co2 = co2.fillna(0)
#gdp = gdp.fillna(0)

del co2['Country Code']
del co2['Indicator Name']
del co2['Indicator Code']
co2 = co2.transpose()

co2.to_csv('co2re.csv')

del gdp['Country Code']
del gdp['Indicator Name']
del gdp['Indicator Code']

gdp = gdp.transpose()
gdp.to_csv('gdpre.csv')