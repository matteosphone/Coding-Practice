# ======================================
# 📊 `pd.DataFrame` Method Drill Set 
# ======================================

#%%
import pandas as pd

df = pd.DataFrame({
    "product": ["A", "B", "C", "B", "A", "B"],
    "sales": [100, 200, 300, 200, 150, 200],
    "region": ["East", "West", "East", "West", "East", "East"],
    "date": [
        "2024-01-01", "2024-01-03", "2024-01-05",
        "2024-02-10", "2024-02-15", "2024-02-20"
    ]
})
#%% 
# --------------------------------------
# Problem 1: View the first few rows
# --------------------------------------
# Task:
# Return the first 3 rows of the DataFrame

# Your code here

df.head(3)

# --------------------------------------
# Problem 2: Drop a column
# --------------------------------------
# Task:
# Drop the "region" column from the DataFrame, without modifying it in place

# Your code here

df.drop(columns='region', inplace=False)

# --------------------------------------
# Problem 3: Sort rows by "sales" descending
# --------------------------------------
# Task:
# Return the DataFrame sorted by the "sales" column from highest to lowest

# Your code here

df.sort_values('sales', ascending=False)

# --------------------------------------
# Problem 4: Convert the "date" column to datetime
# --------------------------------------
# Task:
# Convert the "date" column to datetime format

# Your code here
#%%
df['Date'] = pd.to_datetime(df['date'])
#%%
# --------------------------------------
# Problem 5: Group by "product" and compute total sales
# --------------------------------------
# Task:
# Group the data by "product" and sum the sales for each product

# Your code here

print(df.groupby('product').agg('sum')['sales'])

# --------------------------------------
# Problem 6: Count missing values per column
# --------------------------------------
# Task:
# Return a count of null (missing) values per column

# Your code here

df.isna().sum()

# --------------------------------------
# Problem 7: Remove any duplicate rows
# --------------------------------------
# Task:
# Drop duplicate rows from the DataFrame

# Your code here

df.drop_duplicates()

# --------------------------------------
# Problem 8: Pivot table — product as rows, region as columns
# --------------------------------------
# Task:
# Create a pivot table showing total sales per product-region combo

# Your code here

print(df.pivot_table(index='product', columns='region', values='sales', aggfunc='sum'))

# --------------------------------------
# Problem 9: Check if the DataFrame is empty
# --------------------------------------
# Task:
# Determine if `df` contains zero rows

# Your code here

df.empty

# --------------------------------------
# Problem 10: Convert column names to a regular Python list
# --------------------------------------
# Task:
# Extract the column names as a plain Python list

# Your code here

col_names = list(df.columns)

# --------------------------------------
# Problem 11: Return last 2 rows of the DataFrame
# --------------------------------------
# Task:
# Use the appropriate method to display the last two rows

# Your code here

df.tail(2)

# --------------------------------------
# Problem 12: Get a concise summary of the DataFrame
# --------------------------------------
# Task:
# Print info about columns, non-null counts, and memory usage

# Your code here

df.info()

# --------------------------------------
# Problem 13: Generate descriptive statistics
# --------------------------------------
# Task:
# Get summary stats for all numeric columns

# Your code here

df.describe()

# --------------------------------------
# Problem 14: Remove rows with any missing values
# --------------------------------------
# Task:
# Drop any rows in the DataFrame that contain NaNs

# Your code here
#%%
df = df.dropna()
#%%
# --------------------------------------
# Problem 15: Fill missing values with a constant
# --------------------------------------
# Task:
# Fill NaNs with the number 0

# Your code here

df = df.fillna(0)

# --------------------------------------
# Problem 16: Clip sales values between 100 and 250
# --------------------------------------
# Task:
# Cap the 'sales' column so that all values fall between 100 and 250

# Your code here

df['sales'] = df['sales'].clip(100, 250)

# --------------------------------------
# Problem 17: Find duplicated rows
# --------------------------------------
# Task:
# Return a boolean Series marking duplicate rows

# Your code here
#%%
df.duplicated()
#%%

# --------------------------------------
# Problem 18: Drop duplicate rows
# --------------------------------------
# Task:
# Remove duplicate rows from the DataFrame

# Your code here
#%%
df = df.drop_duplicates()

# --------------------------------------
# Problem 19: Filter DataFrame using SQL-like expression
# --------------------------------------
# Task:
# Select rows where sales are greater than 150 

# Your code here
#%%
print(df.query('sales > 150'))

# --------------------------------------
# Problem 20: Perform a left join on another DataFrame
# --------------------------------------
# Task:
# Merge `df` with `df2` on 'product', keeping all rows from `df`

df2 = pd.DataFrame({
    "product": ["A", "B", "D"],
    "category": ["Phone", "Tablet", "Accessory"]
})

# Your code here
df_merged = df.merge(df2, on='product', how='left')

df_merged
#%%

# --------------------------------------
# Problem 21: Set the index to the "date" column
# --------------------------------------
# Task:
# Set the DataFrame's index to the "date" column

# Your code here
df.set_index('date', inplace=True)

# --------------------------------------
# Problem 22: Reset the index back to default integer index
# --------------------------------------
# Task:
# Move the date index back into a regular column

# Your code here

df.reset_index(inplace=True)

# --------------------------------------
# Problem 23: Sort the DataFrame by index
# --------------------------------------
# Task:
# Sort rows based on the current index values
#%%
# Your code here
df = df.sort_index()
#%%
# --------------------------------------
# Problem 24: Check the names of the index levels
# --------------------------------------
# Task:
# Print the names of the index level(s)
#%%
# Your code here
print(df.index.names)
#%%
# --------------------------------------
# Problem 25: Group by both "product" and "region"
# --------------------------------------
# Task:
# Group the data by both columns and calculate total sales

# Your code here
#%%

multi_df = df.groupby(['product', 'region'])['sales'].sum()

print(multi_df.index)

#%%
# --------------------------------------
# Problem 26: Apply a custom row-level function
# --------------------------------------
# Task:
# Write a row-wise `apply()` that returns "High" if sales > 200, else "Low"

# Your code here
#%%
df['Sales Level'] = df.apply(lambda row: 'High' if row['sales']>200 else 'Low', axis=1)
print(df)
#%%

# --------------------------------------
# Problem 27: Add a derived column using `.assign()`
# --------------------------------------
# Task:
# Create a new column "sales_taxed" which is 1.1 × "sales" using `assign()`

# Your code here
#%%
df = df.assign(sales_taxed = df['sales'] * 1.1)
print(df)
#%%
# --------------------------------------
# Problem 28: Aggregate multiple stats with `.agg()`
# --------------------------------------
# Task:
# Group by "product" and return both mean and max of "sales"

# Your code here

#%%
print(df.groupby('product')['sales'].agg(['mean', 'max']))
#%%

# --------------------------------------
# Problem 29: Rename the DataFrame's index
# --------------------------------------
# Task:
# Set a custom name for the index (e.g., "TransactionDate")

# Your code here

df.index.name = 'TransactionDate'

# --------------------------------------
# Problem 30: Create a MultiIndex by setting two columns as index
# --------------------------------------
# Task:
# Use both "product" and "region" as a hierarchical index

# Your code here
#%%
df = df.set_index(['product','region'])
#%%
