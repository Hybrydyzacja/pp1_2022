# Create a program that writes 50 random integers between 100 and 999 to a text file, 
# each number on a separate line.

import random

with open("random_ints.txt", "a") as file:
    for number in range(1,51):
        x = random.randint(100, 999)
        file.write(str(x))
        file.write("\n")