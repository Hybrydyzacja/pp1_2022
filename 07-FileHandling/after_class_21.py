# Create a program that saves to a text file, numbers in the range of <1,10> with their second and third power.
# Sample result:
# 1,1,1
# 2,4,8
# 3,9,27
# 4,16,64

with open("power.txt", "w", encoding="utf-8") as file:
    for number in range(1, 11):
        file.write(str(number) + "," + str(number**2) + "," + str(number**3))
        file.write("\n")
