with open("countries.txt", "r", encoding="utf-8") as f, open("copylines.txt", "a", encoding="utf-8") as second_f:
    for line in f:
        second_f.write(line)
