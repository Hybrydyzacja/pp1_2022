# Create a program that displays all unique elements in an array. Sample result:
# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

# array = [2,3,2,5,8,1,9,8]
# uniques = []
# for i in array:
#     if (array.count(i)==1):
#         uniques.append(i)

# print(uniques)




def unique_el(array):
    unique = []
    for i in array:
        if (array.count(i)==1):
            unique.append(i)

print(unique_el([2,3,2,5,8,1,9,8]))

