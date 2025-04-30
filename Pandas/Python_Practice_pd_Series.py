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
# %% Problem 8: Use .dropna()
# Create a Series with some missing values
s = pd.Series([10, None, 25, None, 40])

# Task:
# Drop all missing values from the Series
# Your code here:
s_dropna = s.dropna()


# %% Problem 9: Use .map()
# Create a Series of letter grades
s = pd.Series(["A", "B", "C", "A", "F"])

# Task:
# Map the grades to GPA points: A=4, B=3, C=2, F=0
# Your code here:
mapped_gpa = { "A": 4,
               "B": 3,
               "C": 2,
               "D": 1,
               "F": 0
}

s_mapped = s.map(mapped_gpa)

# %% Problem 10: Use .apply()
# Create a Series of numbers
s = pd.Series([10, 15, 20, 25])

# Task:
# Multiply each value by 2 using a lambda function with .apply()
# Your code here:

s_2 = s.apply(lambda x: x*2)


# %% Problem 11: Use .unique()
# Create a Series of repeated categories
s = pd.Series(["x", "y", "x", "z", "y", "x"])

# Task:
# Return the unique values in the Series
# Your code here:

s_unique = s.unique()

# %% Problem 12: Use .nunique()
# Create a Series of repeated categories
s = pd.Series(["x", "y", "x", "z", "y", "x"])

# Task:
# Return the number of unique values in the Series
# Your code here:

s_nunique = s.nunique()

# %% Problem 13: Use .between()
# Create a Series of ages
s = pd.Series([18, 21, 16, 30, 45])

# Task:
# Return a Boolean Series for values between 18 and 30 (inclusive)
# Your code here:

s_18_30 = s.between(18, 30)

# %% Problem 14: Use .shape
# Create a Series of 10 random numbers
s = pd.Series([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# Task:
# Return the shape of the Series
# Your code here:

s.shape

# %% Problem 15: Use .name
# Create a named Series
s = pd.Series([1, 2, 3], name="Sales")

# Task:
# Retrieve the name of the Series
# Your code here:

s.name
# %% Problem 21: Use .pct_change()

# Create a Series of monthly user counts
s = pd.Series([1000, 1100, 1050, 1200])

# Task:
# Return the percent change in users from the previous month
# Your code here:
s.pct_change().dropna()


# %% Problem 22: Use .rolling()
# Create a Series of daily revenue
s = pd.Series([200, 220, 250, 210, 260, 270])

# Task:
# Calculate the 3-day rolling average (moving average)
# Your code here:
print(s.rolling(window=3).mean())


# %% Problem 23: Use .expanding()
# Create a Series of monthly sales
s = pd.Series([500, 700, 600, 800])

# Task:
# Calculate the expanding mean (mean up to each point)
# Your code here:

s.expanding().mean()

# %% Problem 24: Use .size
# Create a Series of product IDs
s = pd.Series(["A1", "A2", "A3", "A4", "A5"])

# Task:
# Return the total number of elements in the Series
# Your code here:

s.size

# %% Problem 25: Use .index
# Create a Series of temperatures
s = pd.Series([72, 68, 75, 70])

# Task:
# Return the index of the Series
# Your code here:

s.index # What does this tell me?

# %% Problem 26: Use .dtype
# Create a Series of boolean flags
s = pd.Series([True, False, True])

# Task:
# Return the data type of the Series
# Your code here:

s.dtype

# %% Problem 27: Use .dt accessor
# Create a Series of datetime strings
dates = pd.Series(["2024-01-01", "2024-01-05", "2024-01-10"])
dates = pd.to_datetime(dates)

# Task:
# Extract the day of the month from each date
# Your code here:

dates.dt.day

# %%
