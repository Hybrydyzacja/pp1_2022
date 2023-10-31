array = [-15, 8, -31, 47, -2, 19]

min = array[0]
max = array[0]

for i in range(len(array)):
    if array[i] < min:
        min = array[i]
    elif array[i] > max:
        max = array[i]

print(min)
print(max)
