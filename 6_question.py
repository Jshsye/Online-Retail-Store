# How many unique customers made purchases?

import pandas as pd
import matplotlib.pyplot as plt

file= pd.read_csv('OnlineRetail.csv', encoding='latin1')
pd.set_option('display.max_columns', None)


un_customer= file['CustomerID'].nunique()
print(f'Unique Customer: {un_customer}')