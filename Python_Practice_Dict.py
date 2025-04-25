"""
Python Practice: Letter Counting
Simple utility functions to count letters in words or phrases.
"""
# %%  Coding challenge: Count letters practice
def count_letters(word): 
    """
    Returns a dictionary with the count of each letter in the given word.
    """
    dic_letters = {}
    for letter in word:
        dic_letters[letter] = dic_letters.get(letter, 0) + 1
    return dic_letters

# Sample usage
word = "apple"
print(f"The total count of the letters within '{word}' is {count_letters(word)}")


def letter_counts(word):
    """
    Case-insensitive version of count_letters.
    Returns letter counts for the given word or phrase.
    """
    lc_dict = {}
    for letter in word.lower():
        if letter.isalpha():  # Optional: Only count alphabetic characters
            lc_dict[letter] = lc_dict.get(letter, 0) + 1
    return lc_dict

# %% New approach to letter_counts() function

def report_letter_counts(text): 
    """
    Formats the letter counts and letters in a more readable format
    """
    sentences = []
    counts = letter_counts(text)
    for letter, freq in counts.items():
        sentences.append(f'Letter: {letter} - Count: {freq}')
    return "\n".join(sentences)

# Test run
print(report_letter_counts('HeLlo'))


# %% Another dictionary challenge

# List of sales transactions (rep name + region sold in)

sales = [
    {"rep": "Alice", "region": "North"},
    {"rep": "Bob", "region": "South"},
    {"rep": "Alice", "region": "North"},
    {"rep": "Diana", "region": "West"},
    {"rep": "Bob", "region": "South"},
    {"rep": "Diana", "region": "West"},
    {"rep": "Alice", "region": "East"}
]

# Return a dictionary where each sales rep maps to their total # of sales

def count_sales_by_rep(data):
    sales_by_rep = {}
    for sale in data:
        sales_by_rep[sale["rep"]] = sales_by_rep.get(sale["rep"], 0) + 1
    return sales_by_rep

print(count_sales_by_rep(sales))
    


# %% Series of quesitons to answer

# 1. What does this return?
d = {"a": 1, "b": 2}
print(d.get("c"))

# None

# 2. Rewrite this using .get() instead of if/else:
# if "x" in d:
#     value = d["x"]
# else:
#     value = 0

# value = d.get('x', 0)

# 3. Fill in the blank to loop over both keys and values:
# for key, value in d.items():
#     print(f'Key: {key}, Value: {value}\n')


# 4. What happens if you try this?
d = {"a": 1}
print(d["b"])

# Error message

# 5. How do you remove the key "x" from a dictionary d and get its value at the same time?

# d.pop("x")

# 6. You want to add multiple new keys to an existing dictionary. What method do you use?

# d.update(new_dictionary)

# 7. What's the result of this?
d = {"a": 1}
d.update({"a": 5, "b": 10})
print(d)

# {"a": 5, "b": 10}

# 8. What's the output?
d = {"a": 1, "b": 2}
print(list(d.keys()))

# ["a", "b"]

# 9. How do you create a shallow copy of a dictionary called original?

# original = d.copy()

# 10. What does this do?
len({"x": 1, "y": 2, "z": 3})

# Measures the number of key value pairs in that dictionary