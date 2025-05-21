# Question:- Find the top 10 products that sold the most (sum of Quantity), sorted in descending order.

import pandas as pd
import matplotlib.pyplot as plt

file= pd.read_csv('OnlineRetail.csv', encoding='latin1')
pd.set_option('display.max_columns', None)
print(file.head())

top_10=file.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
print(top_10)