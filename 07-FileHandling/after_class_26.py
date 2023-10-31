# Find any text file on the Internet and download it to your computer.
# Then write a program that displays all words with at least six letters from the file.
# Display each word on a separate line. Use regular expressions.

import re
with open("masseffect.txt", "r", encoding="utf-8") as file:
    file_content = file.read()

    long_words = re.findall("\w{6}", file_content)
    for word in long_words:
        print(word)
