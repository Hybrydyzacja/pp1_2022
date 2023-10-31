with open("intigers.txt", "w", encoding="utf-8") as file:
    for number in range(1,51):
        file.write(str(number))
        file.write("\n")
