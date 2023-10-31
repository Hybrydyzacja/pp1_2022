# The payment card is secured with a four-digit PIN code (0805).
# Write a program that checks if the PIN code entered in the payment terminal is correct. The user has up to three possibilities for entering a PIN code.
# In case of three unsuccessful attempts, the card is blocked. Sample result:
# Enter the PIN code: 2398
# Incorrect...
# Enter the PIN code: 0912
# Incorrect...
# Enter the PIN code: 7860
# Incorrect...
# Sorry, your payment card has been blocked.


pin = "0805"
user_try = 1

for user_try in range(3):
    user_pin = str(input("Podaj pin: "))
    user_try += 1
    if user_pin == pin:
        break
    elif user_pin != pin and user_try < 3:
        print("Incorrect...")
    elif user_try >= 3:
        print("Incorrect...")
        print("Tarapty, konto zablokowane")
        break


# ?????????????????????????????????????????
# def f(pin, pinn, pinnn):
#     user_pin = str(pin)
#     user_pinn = str(pinn)
#     user_pinnn = str(pinnn)
#     user_try = 1
#     for user_try in range(3): 
#         user_try += 1
#         if user_pin == pin or user_pinn == pin or user_pinnn == pin:
#             break
#         elif user_pin != pin and user_pinn != pin and user_pinnn != pin and user_try < 3:
#             print("Incorrect...")
#         elif user_try >= 3:
#             print("Incorrect...")
#             print("Tarapty, konto zablokowane")
#             break

# f(1246, 1258, 6666)
