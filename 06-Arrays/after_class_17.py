array = [8, 2, 5, 1, 9]

i = 0
for n in array:
    array[i] = n**2
    i += 1
print(array)


# for i in range(len(array)):
#     array[i] = array[i] ** 2
# print(array)

def f(array):
    for i in range(len(array)):
        array[i] = array[i] ** 2
    return(array)

print(f([8, 2, 5, 1, 9]))


print(array)
