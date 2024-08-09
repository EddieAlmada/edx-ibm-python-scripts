################################################## Introduction to Data Visualization ########################################

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_canada = pd.read_excel(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\visualizing_data_with_python\Canada.xlsx', sheet_name= 'Canada by Citizenship',
skiprows= range(20))

df_canada.columns
df_canada.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_canada.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)

df_canada.set_index('Country', inplace = True)
df_canada['Total'] = df_canada.sum(axis=1)
df_canada.columns = list(map(str, df_canada.columns))

years = list(map(str,range(1980,2014)))

df_canada.loc['Haiti',years].plot(kind = 'line')

plt.title('Immigration from Haiti')
plt.xlable('Years')
plt.xlable('Years')

plt.show()

df_canada['2013']

df_canada['2013'].plot(kind = 'hist')

plt.title('Histogram of Immigrants from 195 countries in 2013')
plt.xlable('Number of Countries')
plt.xlable('Number of Immigrants')

plt.show()

