#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

#import csv file
df = pd.read_csv('data.csv')

#group by purpose
df_by_purpose = df.groupby('purpose')

#calculate mean of each column
df_mean = df_by_purpose.mean()

#extract mean interest rates
#convert series to dataframe object
results = df_mean['int_rate'].to_frame()

#rename columns
results = results.rename(columns = {'int_rate':'avg_rate'})

#plots result into a graph
#graph customization 
graph = results.plot(kind='bar', y='avg_rate', legend = False, color = 'orange')
graph.set_ylabel('Average Interest Rate')
graph.yaxis.grid(color = '1.00')
graph.set_facecolor('0.90')
graph.set_axisbelow(True)

#saves figure
plt.savefig('output.pdf', bbox_inches = 'tight')

#save dataframe to csv file
results.to_csv('output.csv')