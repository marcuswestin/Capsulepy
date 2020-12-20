# First, you need to install pip
# Google it
# Then, you need "pip install english_words"
# We'll talk about it

from english_words import english_words_set

# This does a linear search. There are better ways.
# Let's talk about Big-O notation, and how to search
# through a list quickly through binary search
def get_alphabetical_number_of_word(target_word):
    for i, word in enumerate(english_words_set):
        if word == target_word:
            return i
    return -1

print(get_alphabetical_number_of_word('table'))