array = [[True, False], [True, True], [False, False]]

i = 0
for n in array:
    for i in range(len(n)):
        n[i] = not n[i]
    # print(n)
    

print(array)



