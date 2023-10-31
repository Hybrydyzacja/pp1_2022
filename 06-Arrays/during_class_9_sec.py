# An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy.
# Create a program that displays the longest name (consisting of the largest number of characters).

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
names_str = " ".join(names)
print(f"Names: {names_str}")

len_min = len(names[0])
for name in names:
    if len(name) > len_min:
        print(f"Longest name: {name}")
