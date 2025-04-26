# %% The purpose of this python file is to re-look at string methods

# %% STRING METHODS REVIEW

# 1. Turn this string into lowercase
s = "Hello World"
# Your code here:
s_lower = s.lower()

# 2. Turn this string into uppercase
s = "goodbye"
# Your code here:
s_upper = s.upper()

# 3. Remove spaces at the beginning and end
s = "   data science   "
# Your code here:
s_stripped = s.strip()

# 4. Replace all "-" with " "
s = "data-science-is-fun"
# Your code here:
s_space = s.replace('-', ' ')

# 5. Split this string into a list
s = "apple,banana,cherry"
# Your code here:
s_list = s.split(',')

# 6. Join this list into a single string separated by "|"
lst = ["red", "green", "blue"]
# Your code here:
lst_string = '|'.join(lst)

# 7. Check if the string starts with "data"
s = "data analytics"
# Your code here:
s_data = s.startswith('data')

# 8. Check if the string ends with "science"
s = "big data science"
# Your code here:
s_science = s.endswith('science')

# 9. Find the position of the first occurrence of "a"
s = "analytics"
# Your code here:
s_pos = s.find('a')

# 10. Count how many "a" characters are in the string
s = "analytics"
# Your code here:
a_count = s.count('a')

# 11. Check if this string is all alphabetic
s = "MachineLearning"
# Your code here:
s_alpha = s.isalpha()

# 12. Check if this string is all digits
s = "2024"
# Your code here:
s_num = s.isdigit()

# 13. Check if this string is alphanumeric
s = "Python3"
# Your code here:
s_alnum = s.isalnum()

# 14. Title case this sentence
s = "data science is awesome"
# Your code here:
s_title = s.title()

# 15. Capitalize this sentence (only the first letter)
s = "machine learning is the future"
# Your code here:
s_capital = s.capitalize()

# 16. Pad this string with zeros to make it 6 characters wide
s = "42"
# Your code here:
s_zeros = s.zfill(6)

# 17. Get the length of this string
s = "artificial intelligence"
# Your code here:
s_len = len(s)

# 18. Get the type of this object
s = "NLP"
# Your code here:
s_type = type(s)

# 19. Slice to get the first 4 characters
s = "machine"
# Your code here:
s_f4 = s[0:4]

# 20. Slice to get the last 3 characters
s = "learning"
# Your code here:
s_l3 = s[-3:]

# 21. Reverse the string
s = "DeepLearning"
# Your code here:
s_reversed = s[::-1]

# 22. Clean and split this messy string
s = "   hello, world, python  "
# Strip spaces and split by commas
# Your code here:
s_cleaned = s.strip().split(',')

# 23. Check if "data" is **in** the string
s = "big data analytics"
# Your code here:
s_data = 'data' in s

# 24. Using a list comprehension: turn this list of words into their uppercase forms
words = ["data", "science", "python"]
# Your code here:
words_upper = [word.upper() for word in words]

# 25. Using a list comprehension: filter only the alphabetic strings
items = ["AI", "2024", "ML", "123", "DL"]
# Your code here:
items_alpha = [alpha for alpha in items if alpha.isalpha()]

# %%
