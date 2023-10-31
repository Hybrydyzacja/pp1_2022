array = [1, 2, 3, 4, 5, 6, 7]

i = 0
even = 0
odd = 0
while i < len(array):
    if array[i] % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

print(even)
print(odd)