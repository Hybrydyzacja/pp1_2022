file = open("shopping.txt", "a", encoding="utf-8")

item = input("Co chcesz kupić?")

file.write("\n")
file.write(item)

file.close()