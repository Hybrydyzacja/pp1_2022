def suma(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)  #dostajemy 12,3 reszta 3, drugie przejście 1,2 reszta 2
        n = int(n/10)            #dostajemny 123/10 = 12, 12/10 = 1

    return sum


print(suma(1234))
