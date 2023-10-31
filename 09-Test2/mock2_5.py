
def f(first_letter, last_letter):
    import re
    with open("data.txt", "r", encoding="utf-8") as file:
        student_data = file.read()

    array = []
    data_from_file = re.findall("\w+", student_data)
    i = 0
    while i < len(data_from_file):
        for word in data_from_file:
            if word[0] == first_letter and word[-1] == last_letter:
                array.append(word)
        i += 1
        return(len(array))


print(f("w", "d"))
