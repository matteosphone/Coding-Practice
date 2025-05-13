# ======================================
# 📊 NumPy `ndarray` Method Drill Set
# ======================================

#%%
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
#%%

# --------------------------------------
# Problem 1: Check shape, size, ndim
# --------------------------------------
# Task:
# Print the shape, size, and number of dimensions of `arr`

print(arr.shape, arr.size, arr.ndim)

# --------------------------------------
# Problem 2: Get dtype and itemsize
# --------------------------------------
# Task:
# Print the data type and bytes per element of `arr`
#%% 
print(arr.dtype, arr.itemsize)

# --------------------------------------
# Problem 3: Flatten array to 1D (view)
# --------------------------------------
# Task:
# Flatten `arr` using `.ravel()`
#%%
print(arr.ravel())
#%%
# --------------------------------------
# Problem 4: Flatten array to 1D (copy)
# --------------------------------------
# Task:
# Flatten `arr` using `.flatten()`
#%%
print(arr.flatten())
#%%
# --------------------------------------
# Problem 5: Reshape to 1 row, 9 columns
# --------------------------------------
# Task:
# Reshape `arr` to shape (1, 9)
#%%
print(arr.reshape(9, 1))
#%%
# --------------------------------------
# Problem 6: Sum of each column
# --------------------------------------
# Task:
# Compute the sum of `arr` along columns (axis=0)
#%%
print(arr.sum(axis=0))
#%%
# --------------------------------------
# Problem 7: Mean of each row
# --------------------------------------
# Task:
# Compute the mean of `arr` along rows (axis=1)
#%%
print(arr.mean(axis=1))
#%%

# --------------------------------------
# Problem 8: Clip values between 3 and 7
# --------------------------------------
# Task:
# Clip `arr` values so everything falls between 3 and 7
#%%
print(arr.clip(3, 7))
#%%

# --------------------------------------
# Problem 9: Replace values > 5 with 99
# --------------------------------------
# Task:
# Use `np.where` to replace values greater than 5 with 99
#%%
print(np.where(arr>5, 99, arr))
#%%
# --------------------------------------
# Problem 10: Get index of max element
# --------------------------------------
# Task:
# Find index of the maximum value in `arr`
#%%
print(np.argmax(arr))
#%%

# --------------------------------------
# Problem 11: Create random array of shape (3, 4)
# --------------------------------------
# Task:
# Generate uniform random floats in [0, 1) of shape (3, 4)

# --------------------------------------
# Problem 12: Draw 5 samples from normal distribution
# --------------------------------------
# Task:
# Generate 5 samples from standard normal distribution

# Your code here

# --------------------------------------
# Problem 13: Elementwise multiply by 10
# --------------------------------------
# Task:
# Multiply `arr` elementwise by 10 using `np.multiply`

# Your code here

# --------------------------------------
# Problem 14: Logical mask for values < 5
# --------------------------------------
# Task:
# Create boolean mask where `arr < 5`

# Your code here

# --------------------------------------
# Problem 15: Logical AND mask for values between 3 and 7
# --------------------------------------
# Task:
# Create boolean mask where `arr >= 3` AND `arr <= 7`

# Your code here

# --------------------------------------
# Problem 16: Vertically stack `arr` with itself
# --------------------------------------
# Task:
# Use `np.vstack` to stack `arr` on top of itself

# Your code here

# --------------------------------------
# Problem 17: Horizontally stack `arr` with itself
# --------------------------------------
# Task:
# Use `np.hstack` to stack `arr` side by side with itself

# Your code here

# --------------------------------------
# Problem 18: Concatenate along axis 0
# --------------------------------------
# Task:
# Concatenate `[arr, arr]` along axis=0 using `np.concatenate`

# Your code here

# --------------------------------------
# Problem 19: Split a 1D array into 3 chunks
# --------------------------------------
# Task:
# Create `a = np.arange(12)` and split into 3 equal chunks

# Your code here

# --------------------------------------
# Problem 20: Transpose the original array
# --------------------------------------
# Task:
# Return the transpose of `arr` using `.T`

# Your code here

#%%
