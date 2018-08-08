import pandas as pd
import numpy as np

data = pd.read_excel('smple tracking.xlsx')
#print(data[0:7])
#print(data['Customer Email'])

# Create merged dataframe by adding the first customer
merged = data.iloc[[0]]
all_orders = data.loc[data['Customer Email'] == merged.loc[0, 'Customer Email']]

# Create additional columns for tracking numbers
new_headers = [f'Tracking Number {i}' for i in range(2, 8)]
merged = merged.reindex(columns = merged.columns.tolist() + new_headers)

for i, number in enumerate(all_orders.loc[1:,'Tracking Number']):
    merged.iloc[0, i+3] = str(number)

#for email in data['Customer Email']:
#    print(data.loc[data['Customer Email'] == email])

    # Make sure that the list is filtered only once on each email
#    if email not in merged['Customer Email']:
#        print(f'Adding customer: {email}')
#        merged.append(data

#


merged = merged.rename(index=str, columns={'To Name':'Name', 
                                    'Customer Email':'Email',
                                    'Tracking Number':'Tracking Number 1',
                                    })
print(merged)
