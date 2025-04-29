# %% Problem 1: Use .value_counts()
import pandas as pd

# Create a Series
s = pd.Series(["cat", "dog", "cat", "bird", "dog", "dog"])

# Task:
# Use a single line of code to count the frequency of each animal
# Your code here:

print(s.value_counts())

# %% Problem 2: Use .fillna()
# Create a Series with missing values
s = pd.Series([2, None, 5, None, 8])

# Task:
# Fill all missing (None) values with 0
# Your code here:
print(s.fillna(0))


# %% Problem 3: Use .astype()
# Create a Series with string numbers
s = pd.Series(["1", "2", "3", "4"])

# Task:
# Convert this Series to integers
# Your code here:
print(s.astype(int))

# %% Problem 4: Use .replace()
# Create a Series with typos
s = pd.Series(["Nw York", "Los Angeles", "Nw York", "Chicago"])

# Task:
# Replace "Nw York" with "New York" in the Series
# Your code here:
print(s.replace("Nw York", "New York"))


# %% Problem 5: Use .sort_values()
# Create a numeric Series
s = pd.Series([50, 10, 30, 20, 40])

# Task:
# Sort the Series in ascending order
# Your code here:

print(s.sort_values(ascending=True))


# %% Problem 6: Use .str.replace()
# Create a Series of city names with typos
s = pd.Series(["Nw York", "Los Angeles", "Nw York", "Chicago"])

# Task:
# Use .str.replace() to fix "Nw" → "New" inside all string values
# Your code here:

print(s.str.replace("Nw", "New"))

# %% Problem 7: Use .clip()
# Create a Series of exam scores
s = pd.Series([45, 82, 97, 120, 65])

# Task:
# Clip the scores so that all values are between 0 and 100
# (any score over 100 should become 100)
# Your code here:

print(s.clip(0, 100))
# %%
