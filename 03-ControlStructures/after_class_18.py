amount = float(input("Podaj cenę: "))

# amount_of_five = int(amount/5)
# print(f'5zł - {amount_of_five}')
# amount = amount - amount_of_five * 5

# amount_of_two = int(amount/2)
# print(f'2zł - {amount_of_two}')
# amount = amount - amount_of_two *2

# amount_of_one = int(amount/1)
# print(f'1zł - {amount_of_one}')


# if amount % 5 != 0:
#     five = int(amount / 5)
#     print(f"5zł - {five}")
#     amount = amount - (five * 5)
#     # print(amount)
#     if amount % 2 != 0:
#         two = int(amount / 2)
#         print(f"2zł - {two}")
#         amount = amount - (two * 2)
#         one = int(amount/1)
#         print(f'1zł - {one}')
# else:
#     five = int(amount / 5)
#     print(f"5zł - {five}")
#     print("2zł - 0")
#     print("1zł = 0")

five = int(amount / 5)
amount_a_f = amount - (five * 5)   #a_f = after five
two = int(amount_a_f / 2)
amount_a_t = amount_a_f - (two * 2)  #a_t = after two
one = int(amount_a_t/1)

if amount % 5 != 0 or amount % 2 != 0:
    print(f"5zł - {five}")
    print(f"2zł - {two}")
    print(f'1zł - {one}')
else:
    print(f"5zł - {five}")
    print("2zł - 0")
    print("1zł - 0")

# def f(amount):
#     five = int(amount / 5)
#     amount_a_f = amount - (five * 5)  
#     two = int(amount_a_f / 2)
#     amount_a_t = amount_a_f - (two * 2)  
#     one = int(amount_a_t/1)
#     if amount % 5 != 0 or amount % 2 != 0:
#         coins = (f"5zł - {five},  2zł - {two}, 1zł - {one}")    
#     else:
#         coins = (f"5zł - {five}, 2zł - 0, 1zł - 0 ")
#     return coins
      