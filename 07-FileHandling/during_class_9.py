numbers = open("numbers.txt", "r")

sum = 0
for number in numbers:
    sum = sum + int(number)

numbers.close()
print(sum)  #najpierw zamknąć, później printowac