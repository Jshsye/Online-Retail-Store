#  Count how many invoices are cancelled (these usually start with 'C' in InvoiceNo).

import pandas as pd
import matplotlib.pyplot as plt

file= pd.read_csv('OnlineRetail.csv', encoding='latin1')
pd.set_option('display.max_columns', None)


file['status']= file['InvoiceNo'].astype(str).str.startswith('C')
file['status']= file['status'].replace({True: 'Cancelled', False: 'Completed'})

cancelled_count= file[file['status']== 'Cancelled']['InvoiceNo'].nunique()

print(f'Total Number of orders Cancelled: {cancelled_count}')