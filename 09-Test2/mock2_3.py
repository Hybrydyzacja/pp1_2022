def f(array2D):

    sum = 0
    array = []
    for j in range(len(array2D)+1):
        for i in range(len(array2D)):
            sum += array2D[i][j]
        array.append(sum)
        sum = 0
    return(array)


    # sum = 0
    # array = []
    # for j in range(len(array2D)):
    #     for i in range(len(array2D)+1):
    #         sum += array2D[j][i]
    #     array.append(sum)
    #     sum = 0
    # return(array)




print(f([[3, 6, 2,7 ], [9, 5, 4, 0], [2, 8, 0, 9]]))
