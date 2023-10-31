height_cm = float(input("Podaj swój wzorst (cm): "))
height_inch = height_cm * 0.3937
# print(height_inch)
height_feet = height_inch/12
# print(height_feet) 

height_feet_round = int(round(height_inch//12,1))
# print(height_feet_round)

height_inches_round = int(round((height_feet - (height_inch//12)) * 12,1))
# print(height_inches_round)

print(f"I am {height_cm}cm tall, i.e. {height_feet_round} feet and {height_inches_round} inches.")
