# Define a function compare(array1, array2) that returns True if both arrays are the same.
# Arrays are the same if they have the same number of elements
# and values of elements in cells of arrays with the same index are equal.
# Then create a program and try to compare the following arrays:
# a.	["water","book","sky"]   ["water","book","sky"]
# b.	[True,False]   [True,False,True]
# c.	[5,3,1]   [5,3,1]
# d.	[3,2,1]   [3,2]

def compare(array1, array2):
    # return(array1 == array2)
    if (array1 == array2) == True:
        return(f"Array1 {array1}\nArray2 {array2}\nComparison: arrays are the same")
        # return(True)
    else:
        return(f"Array1 {array1}\nArray2 {array2}\nComparison: arrays are different")
        # return(False)


print(compare(["water", "book", "sky"], ["water", "book", "sky"]))
print()
print(compare([True, False], [True, False, True]))
print()
print(compare([5, 3, 1], [5, 3, 1]))
print()
print(compare([3, 2, 1], [3, 2]))
