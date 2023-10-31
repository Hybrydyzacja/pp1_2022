
# Write a program that creates the following pattern. Sample result:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


# for number in range(0, 6):
#     print(("*" + " ") * number)
# for number in range(6, 0, -1):
#     print(("*" + " ") * number)


def pattern():
    for number in range(0, 6):
        print(("*" + " ") * number)
    for number in range(6, 0, -1):
        print(("*" + " ") * number)

pattern()

# def pattern():
#     for number in range(0, 6):
#         wynik = (("*" + " ") * number)
#     for number in range(6, 0, -1):
#         wynik = (("*" + " ") * number)
#     return wynik
         
