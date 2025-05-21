# Extract hour from InvoiceDate and find which hour of the day has the most purchases.
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('OnlineRetail.csv', encoding='latin1')
pd.set_option('display.max_columns', None)


file['InvoiceDate'] = pd.to_datetime(file['InvoiceDate'])

file['Hour'] = file['InvoiceDate'].dt.hour

hourly_orders = file['Hour'].value_counts().sort_index()

print(hourly_orders)

plt.figure(figsize=(10,6))
plt.plot(hourly_orders.index, hourly_orders.values, marker='o', color='green')
plt.title('Purchases by Hour of the Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Purchases')
plt.grid(True)
plt.tight_layout()
plt.savefig('Trend of Sales in Hour.png', dpi=300, bbox_inches= 'tight')
plt.show()
