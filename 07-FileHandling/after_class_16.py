with open("countries.txt", "r", encoding="utf-8") as f, open("copy.txt", "w", encoding="utf-8") as second_f:
    second_file = f.read()
    second_f.write(second_file)
