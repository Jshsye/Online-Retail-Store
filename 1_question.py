import pandas as pd
import matplotlib.pyplot as plt

file= pd.read_csv('OnlineRetail.csv', encoding='latin1')
pd.set_option('display.max_columns', None)
# print(file.head())


file['Revenue']= file['Quantity'] * file['UnitPrice']

total_revenue= file['Revenue'].sum()
print(f'Total Revenue:- {total_revenue}')
