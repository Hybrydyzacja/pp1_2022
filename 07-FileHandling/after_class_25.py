# Write a program that computes the number of words in the following text. Use regular expressions.
# To be, or not to be, that is the question

import re

x = "To be, or not to be, that is the question"

words_in_x = re.findall("\w+", x) #samp "w" bez plusa odda liczbe liter
print(len(words_in_x))

