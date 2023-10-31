# f = open("filename.txt", encoding="utf-8")
# for line in f:
#      print(line, end="")
# f.close()

with open("filename.txt", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
