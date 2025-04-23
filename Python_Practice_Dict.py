
def count_letters(word): 
    dic_letters = {}
    for letter in word:
        uniq_letter = word[word == letter]
        dic_letters[letter] = len(uniq_letter)
    
word = "apple"

# How do I continue this line without the tabs showing up in the text? 
print(f"The total count of the letters within '{word}'\
        is {count_letters(word)}")

# %%



# %% Coding challenge 1


def letter_counts(word):
    lc_dict = {}
    for letter in word.lower():
        lc_dict[letter] = lc_dict.get(letter, 0) + 1
    return lc_dict


def report_letter_counts(text): 
    temp_dict = letter_counts(text)
    

    

print(letter_counts('HeLlo'))



# %%
