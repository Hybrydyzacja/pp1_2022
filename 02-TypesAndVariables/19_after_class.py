weight = float(input("Podaj swoją wagę w kg: "))

height = float(input("Podaj swój wzrost w cm: "))

BMI = round(weight/(height/100)**2, 2)

# print(f"Twoja waga wynosi {weight} cm")
# print(f"Twój wzrost to {height} cm")
print(f"Twoje BMI wynosi {BMI}")

if BMI < 18.5:
    print("BMI zbyt niskie")
elif BMI > 24.99:
    print("BMI zbyt wysokie")
else:
    print("BMI jest prawidłowe!")
