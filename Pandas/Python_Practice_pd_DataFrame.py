# ======================================
# 📊 `pd.DataFrame` Method Drill Set 
# ======================================

#%%
import pandas as pd

df = pd.DataFrame({
    "product": ["A", "B", "C", "B", "A"],
    "sales": [100, 200, 300, 200, 150],
    "region": ["East", "West", "East", "West", "East"],
    "date": [
        "2024-01-01", "2024-01-03", "2024-01-05",
        "2024-02-10", "2024-02-15"
    ]
})

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

df['Date'] = pd.to_datetime(df['date'])

# --------------------------------------
# Problem 5: Group by "product" and compute total sales
# --------------------------------------
# Task:
# Group the data by "product" and sum the sales for each product

# Your code here

print(df.groupby('product').agg('sum'))['sales']

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

#%% 
