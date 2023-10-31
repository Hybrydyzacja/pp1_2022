# A user enters two integer numbers from the keyboard. Write a program that checks if at least one of them is positive.

x = int(input("Podaj liczbę pierwszą: "))
y = int(input("Podaj liczbę drugą: "))

if x >= 0 or y >= 0:
    print("Przynajmniej jedna liczba jest dodatnia")
else:
    print("Ani jedna z liczb nie jest dodatnia")
