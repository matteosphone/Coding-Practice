# %% Python Practice Lists

# Level 1: Reviewing the basics

lst = [1, 2, 2, 3, 4]
lst2 = [5, 6, 7, 8]


print(lst.count(2))


# %% Build new list only containing integers and multiply by 10
data = [5, "apple", None, 15, "banana", 20, None, "carrot", 25]
processed_data = [num*10 for num in data if isinstance(num, int)]

print(processed_data)

# %% Split sales into batches of 3 and sum
sales = [100, 200, 300, 400, 500, 600, 700, 800, 900]

chunks = []
for i in range(0, len(sales), 3):
    chunks.append(sum(sales[i:i+3]))


chunks = [sum(sales[i:i+3]) for i in range(0, len(sales), 3)]

print(chunks)

# %% List review Challenge
# Comprehensive script to test list methods, patterns, and attributes

# 1. Build a list of integers 1–5 one at a time (don't hardcode [1,2,3,4,5])
my_list = []
# Your code here:
for num in range(1, 6):
    my_list.append(num)

# 2. Add the elements [6, 7, 8] to the end of your existing list in one command
# Your code here:
my_list.extend([6, 7, 8])

# 3. Insert the string "Start" at the beginning of your list
# Your code here:
my_list.insert(0, 'Start')

# 4. Remove the number 3 by value, not index
# Your code here:
my_list.remove(3)

# 5. Pop and capture the last element into a variable called popped_value
# Your code here:
popped_value = my_list.pop()

# 6. Find and print the index where the number 4 is currently located
# Your code here:
print(my_list.index(4))

# 7. Count how many times 2 appears in your list
# Your code here:
count_two = my_list.count(2)

# 8. Sort your list (ignore non-integer elements for now if needed)
# Your code here:
numeric_list = [num for num in my_list if num != 'Start']
numeric_list.sort()

# 9. Reverse your list in-place
# Your code here:
my_list.reverse()

# 10. Make a shallow copy of the current list and call it new_list
# Your code here:
new_list = my_list.copy()

# 11. Clear all items from the original list
# Your code here:
my_list.clear()

# 12. Check if 5 is in new_list (print True/False)
# Your code here:
print(5 in new_list)

# 13. Using slicing, print the first three elements of new_list
# Your code here:
print(new_list[0:3])

# 14. Using slicing, create a reversed copy of new_list (without modifying new_list)
# Your code here:
reversed_list = new_list[::-1]

# 15. Use a list comprehension to create a list of the squares of numbers from 0–9
# Your code here:
squares = [x**2 for x in range(10)]

# 16. Given a nested list, flatten it using a list comprehension
nested = [[1, 2], [3, 4], [5]]
# Your code here:
unnested_lst = [num for sub_list in nested for num in sub_list]

# 17. Filter out all None values from this list using a list comprehension
messy = [1, None, 2, None, 3, 4, None]
# Your code here:
un_messy = [num for num in messy if num is not None]
