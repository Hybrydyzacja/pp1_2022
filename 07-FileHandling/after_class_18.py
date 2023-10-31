with open("MeatAndFish.txt", "r") as meat, open("GrainsAndBread.txt", "r") as grains, open("shoppinglist.txt", "a", encoding="utf-8") as list_file:
    meat_list = meat.read()
    list_file.write(meat_list)
    grains_list = grains.read()
    list_file.write(grains_list)

    
