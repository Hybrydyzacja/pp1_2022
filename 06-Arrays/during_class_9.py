array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

print(array)
max = array[0]
min = array[0]
i = 0
for name in array:
    if array[i] > max:
        max = array[i]
    elif array[i] < min:
        min = array[i]
    i += 1
print(max)
print(min)