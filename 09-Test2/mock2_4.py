def f(dictionary, x, y):

    sum = 0
    for key in dictionary:
        for value in dictionary[key]:
            if value in range(x, y+1):
                sum += value
            else:
                continue
    return(sum)
    # for wart in range(x, y+1):
    #     return(wart)


print(f({"arr1": [4, 5, 6], "arr2": [7, 5]}, 5, 6))
