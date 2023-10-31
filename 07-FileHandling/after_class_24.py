# Write a program that calculates the number of vowels in the text:
# To be, or not to be, that is the question
# Use regular expressions and the findall() method.

import re

x = "To be, or not to be, that is the question"


# regex = "[aeiou]"
# sum = 0
# for char in x:
# 	if(re.search(regex, char.lower())):
# 		sum += 1
# print(sum)   

vowels_found = re.findall("a|e|i|o|u", x)
print(vowels_found)
print(len(vowels_found))