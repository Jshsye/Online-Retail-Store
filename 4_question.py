# Calculate the total revenue generated from each country. Display the top 5 revenue-generating countries.

import pandas as pd
import matplotlib.pyplot as plt

file= pd.read_csv('OnlineRetail.csv', encoding='latin1')
pd.set_option('display.max_columns', None)


file['revenue']= file['Quantity'] * file['UnitPrice']

total_revenue = file.groupby('Country')['revenue'].sum().sort_values(ascending=False).head(5)

print('Total Revenue Of Top 5 Countries')
print(total_revenue)