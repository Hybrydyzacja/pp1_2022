# Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
# Create a program that displays the numbers from the first array that do not appear in the second array.

first_array = [4,36,12,28,9,44,5]
second_array = [5,1,36]

for i in range(len(first_array)):
        for j in range(len(second_array)):
            if (first_array[i] == second_array[j]):
                break
 
        if (j == len(second_array) - 1) and (first_array[i] != second_array[j]):
            print(first_array[i], end = " ")