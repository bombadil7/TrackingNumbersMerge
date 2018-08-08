import pandas as pd
import numpy as np

data = pd.read_excel('smple tracking.xlsx')
#print(data[0:7])
#print(data['Customer Email'])
#data = data.rename(index=str, columns={'To Name':'Name', 
#                                    'Customer Email':'Email',
#                                    'Tracking Number':'Tracking Number 1',
#                                    })
# Create additional columns for tracking numbers
new_headers = [f'Tracking Number {i}' for i in range(2, 8)]
data = data.reindex(columns = data.columns.tolist() + new_headers)

# Create merged dataframe by adding the first customer
merged = data.iloc[[0]]
all_orders = data.loc[data['Customer Email'] == merged.loc[0, 'Customer Email']]

# Insert additional tracking numbers for the first customer
for i, number in enumerate(all_orders.loc[1:,'Tracking Number']):
    merged.iloc[0, i+3] = number

for index, order in data.iterrows():
    email = order['Customer Email']
    # Make sure that the list is filtered only once on each email
    if  email not in merged.loc[:, 'Customer Email'].unique():
        all_orders = data.loc[data['Customer Email'] == order.loc['Customer Email']]
        for i, number in enumerate(all_orders.loc[1:,'Tracking Number']):
            order.iloc[i+2] = number
        merged = merged.append(order)

merged = merged.rename(index=str, columns={'To Name':'Name', 
                                    'Customer Email':'Email',
                                    'Tracking Number':'Tracking Number 1',
                                    })

merged.set_index('Name', inplace=True)
#print(merged)
merged.to_csv('merged_tracking.csv')
