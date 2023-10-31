# The grades.txt file contains student’s grades. Create the file in any text editor.
# Name: Peter
# Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
# Then create a program that calculates the arithmetic mean of student’s grades.

import re
with open("grades.txt", "r", encoding="utf-8") as file:
    file_content = file.read()
    # print(file_content)
    grades_Peter = re.findall("\d+\.\d+",file_content)
    print(grades_Peter)

    sum = 0
    for grade in grades_Peter:
        sum += float(grade)
        mean = sum / len(grades_Peter)
        
    print(sum)
    print(round(mean,2))