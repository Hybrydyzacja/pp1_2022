with open("films.txt") as f:
    # file_content = f.read()
    sum = 0
    for line in f:
        sum += 1
    print("File name: films.txt")
    print(f"Number of lines: {sum}")
