def f(liczba):
    x = 1
    y = 10
    for number in range (x,y):
        if liczba >= x and liczba <= y:
            return True
        else:
            return False

print(f(11))
