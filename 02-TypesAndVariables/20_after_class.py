from random import randint

dice_roll = randint(1, 6)
dice_roll_sec = randint(1, 6)
dice_roll_thir = randint(1, 6)

print(f"Rzut pierwszy: {dice_roll}")
print(f"Rzut drugi: {dice_roll_sec}")
print(f"Rzut trzeci: {dice_roll_thir}")

# print(dice_roll + dice_roll_sec + dice_roll_thir) - wersja bez napisu
dice_sum = dice_roll + dice_roll_sec + dice_roll_thir
print(f"Suma oczek: {dice_sum}")

