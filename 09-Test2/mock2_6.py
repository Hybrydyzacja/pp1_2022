def f(age, course, average):
    import json
    with open("data.json", "r", encoding="utf-8") as students:
        students_data = json.load(students)

    i = 0
    array_students = []

    while i < len(students_data):
        for student in students_data:
            for stat in student["studies"]["courses"]:
                if stat["name"] == course:
                    average_grad = (sum(stat["grades"]))/len(stat["grades"])
                else:
                    continue

            if student["age"] >= age and average_grad >= average:
                array_students.append(student)
        i += 1
        return(len(array_students))


print(f(21, "statistics", 4))
