# Convert InvoiceDate to datetime, group by month, and plot monthly revenue using matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

file= pd.read_csv('OnlineRetail.csv', encoding='latin1')
pd.set_option('display.max_columns', None)

file["date"]=pd.to_datetime(file['InvoiceDate'])

file['Month']=file['date'].dt.to_period('M')

file['Revenue']= file['Quantity'] * file['UnitPrice']

monthly_revenue = file.groupby('Month')['Revenue'].sum()

# Convert PeriodIndex to datetime for plotting
monthly_revenue.index = monthly_revenue.index.to_timestamp()

plt.plot( monthly_revenue.index, monthly_revenue.values, marker='o', color= 'Blue')
plt.title('Trend of Revenue')
plt.xlabel('Months')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.savefig('Revenue_Trend.png', dpi=300, bbox_inches='tight')
plt.show()