array = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

even = 0
odd = 0
for i in array:
    for n in i:
        if n % 2 == 0:
            even = even + n
        else:
            odd = odd + n

print(even)
print(odd)
