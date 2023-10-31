# The 'university' variable contains the name of university where you study.
# Write a program that displays the contents of the variable with an extra space between characters (add a space between each character).

# university = "UEK w Krakowie"

# for letter in university:
#     print(letter + " ", end="")

# def f(university):
#     final = ""
#     for letter in university:
#         final = final + letter + " "
#     return final

# print(f("UEK w Krakowie"))

def f(university):
    final = ""

    for letter in university:
        final = final + "-" + letter 
    return final[1:]
           


print(f("UEK w Krakowie"))
