"""
Python Practice: Letter Counting
Simple utility functions to count letters in words or phrases.
"""

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

# %% Coding Challenge 1

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

def report_letter_counts(text): 
    """
    Placeholder for reporting logic, to be implemented.
    """
    temp_dict = letter_counts(text)
    # Future: Format and print results nicely
    return temp_dict

# Test run
print(letter_counts('HeLlo'))
