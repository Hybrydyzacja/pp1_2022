# user_number = int(input("Podaj liczbę: "))

# number = 1
# while number < 10:
#     wynik = int(user_number * number)
#     print(f"{user_number} x {number} = {wynik}")
#     number = number + 1

#     if wynik % user_number == 0:
#         print(end = "")

# def f(user_number):
#     number = 1
#     while number < 10:
#         wynik = int(user_number * number)
#         print(f"{user_number} x {number} = {wynik}")
#         number = number + 1
# f(6)

def f(user_number):
    number = 1
    xxx = ""
    while number < 10:
        # for number in range(1, 10):
        wynik = int(user_number * number)
        result = (f"{user_number} x {number} = {wynik}")
        xxx = xxx + result + "\n"
        number = number + 1
    return xxx


print(f(6))
