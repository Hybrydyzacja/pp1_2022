# An array contains integer numbers: 12, 6, 4, 9, 10. 
# Create a program that displays the array values graphically as below. 
# Define a function star(n) that returns the given number of asterisks as a string. 
# Use a defined function in the program.
# 12: ************
#  6: ******
#  4: ****
#  9: *********
# 10: **********


# array = [12, 6, 4, 9, 10]

def star(n):
    for i in range(len(n)):
        n[i] = n[i] * "*"
    return(n)
    
# def star(n):
#     for i in range(len(n)):
#         char = "*"
#         # print(f"{n[i]}: {n[i]*char}")
#         return(f"{n[i]}: {n[i]*char}")
    
# def star(n):
#     i = 0
#     while i < len(n):
#         char = "*"
#         return(f"{n[i]}: {n[i]*char}")  JAK ZWRÓCIĆ WSZYSTKIE PO KOLEI?

    


print(star([12, 6, 4, 9, 10]))
