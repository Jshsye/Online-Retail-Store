#  Identify customers who have generated total revenue greater than 10,000.

import pandas as pd
import matplotlib.pyplot as plt

file= pd.read_csv('OnlineRetail.csv', encoding='latin1')
pd.set_option('display.max_columns', None)

file['Total_revenue']= file['Quantity'] * file['UnitPrice']


customer_revenue= file.groupby('CustomerID')['Total_revenue'].sum()

high_valued_cus = customer_revenue[customer_revenue > 10000]

print(f"Number of customers with revenue > 10,000: {len(high_valued_cus)}")
print(high_valued_cus.sort_values(ascending=False))