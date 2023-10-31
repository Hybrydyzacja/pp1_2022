# def phone_keypad():
#     for number in range(1,4):
#         print(number, end="  ")
#     print()
#     for number in range(4,7):
#         print(number, end="  ")
#     print()
#     for number in range(7,10):
#         print(number, end="  ")

# phone_keypad()

# def phone_keypad():
#     for x in range(1,10,1):
#         if x % 3 == 1:
#             print(x, end="  ")
#         elif x % 3 == 2:
#             print(x, end="  ")
#         else:
#             print()

# phone_keypad()


# def phone_keypad():
#     for i in range(1,10):
#         print(i, end="  ")
#         if i == 3 or i == 6:
#             print()

# phone_keypad()

def phone_keypad():
    for i in range(1,10):
        print(i, end="  ")
        if i % 3 == 0:
            print()

phone_keypad()