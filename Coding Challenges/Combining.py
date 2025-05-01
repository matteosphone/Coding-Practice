# You are given a list of dictionaries representing raw product transactions:
#%%
import pandas as pd

transactions = [
    {"product": "  iPhone_14 Pro  ", "amount": 1200, "timestamp": "2024-05-01"},
    {"product": "Galaxy_S23 ", "amount": 950, "timestamp": "2024-05-03"},
    {"product": "pixel_7  ", "amount": 600, "timestamp": "2024-04-25"},
    {"product": "  iPhone_14 Pro", "amount": 1250, "timestamp": "2024-05-10"},
    {"product": "Pixel_7", "amount": 630, "timestamp": "2024-05-12"},
]

df = pd.DataFrame(transactions)

df['product'] = df['product'].str.strip().str.replace('_', ' ').str.lower()

df['timestamp'] = pd.to_datetime(df['timestamp'])

df['month'] = df['timestamp'].dt.month_name()

count_may = df['month'].value_counts().get('May', 0)

count_may = (df['month']=='May').sum()

print(count_may)

# %%
