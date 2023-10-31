def f(player1, player2):
    
    sum = 0
    sum2 = 0

    for i in range(len(player1)):
        if player1[i] == "A" or player1[i] == "K" or player1[i] == "Q" or player1[i] == "J" or player1[i] == "T":
            sum += 10
        else:
            sum += int(player1[i])

    for j in range(len(player2)):
        if player2[j] == "A" or player2[j] == "K" or player2[j] == "Q" or player2[j] == "J" or player2[j] == "T":
            sum2 += 10
        else:
            sum2 += int(player1[j])

    return(sum > sum2)


print(f("AJ972", "AQT72"))
