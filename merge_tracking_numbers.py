import pandas as pd
import numpy as np
import sys

# TODO: fix warning
# make friendly comments to user when input / output files can't be open
# delete extra columns
# add file name as an optional argument
# try renaming the original frame columns

file_name = 'smple tracking.xlsx'

if len(sys.argv) == 2:
    file_name = sys.argv[1]
# def merge_track_numbers
try:
    data = pd.read_excel(file_name)
except FileNotFoundError:
    print(f"Could not open file {file_name}.\n"
          "Make sure it is located in the same directory as the script.")
    exit()

data.dropna(axis='columns', how='all', inplace=True)
# Create additional columns for tracking numbers
new_headers = [f'Tracking Number {i}' for i in range(2, 10)]
data = data.reindex(columns=data.columns.tolist() + new_headers)

# Create merged dataframe by adding the first customer
merged = data.iloc[[0]].copy()
all_orders = data.loc[data['Customer Email'] == merged.loc[0, 'Customer Email']]

# Insert additional tracking numbers for the first customer
for i, number in enumerate(all_orders.loc[1:, 'Tracking Number']):
    #merged.iloc[0, i+3] = number
    merged.loc[merged.index[0], f'Tracking Number {i+2}'] = number

for index, order in data.iterrows():
    email = order['Customer Email']
    # Make sure that the list is filtered only once on each email
    if email not in merged.loc[:, 'Customer Email'].unique():
        all_orders = data.loc[data['Customer Email'] == order.loc['Customer Email']]
        for i, number in enumerate(all_orders.loc[1:, 'Tracking Number']):
            order.iloc[i+2] = number
        merged = merged.append(order)

merged = merged.rename(index=str, columns={'To Name': 'Name',
                                           'Customer Email': 'Email',
                                           'Tracking Number': 'Tracking Number 1',
                                           })

merged.set_index('Name', inplace=True)
merged.dropna(axis='columns', how='all', inplace=True)
# print(merged)
out_file_name = 'merged_tracking.csv'
try:
    merged.to_csv(out_file_name)
    print(f"Output written to file {out_file_name}")
except PermissionError:
    print(f"Could not open file {out_file_name} for writing.\n"
          "Check if it is open already.")
    exit()
