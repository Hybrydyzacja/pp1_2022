array = [1,2,3,4,5]

array[0] = array[0] - 1
print(array)

array[-1] = array[-1] + 4
print(array)

# array[len(array)-1] = array[len(array)-1] + 4
# print(array)
array[len(array)//2] = array[len(array)//2] * 2
print(array)

for i in range(len(array)):
    array[i] = array[i] + 3
print(array)
