# The variables a and b contain the dimensions of the sides of the rectangle. 
# Write a program that creates the following rectangle with dimensions a and b. Example result for a = 4 and b = 15:
# ***************
# *             *
# *             *
# ***************


a = int(input("Podaj długość boku a: "))
b = int(input("Podaj długośc boku b: "))

number = 0
while number <= (a - 1):
    number += 1
    if number == 1 or number == a:
        print("*" * b)
    else:
        print ("*" + " " * (b - 2) + "*")

