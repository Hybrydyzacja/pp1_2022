# Using the website https://mockaroo.com, generate a list of 500 students, containing the following data:
# name, surname, student ID, gender, age, year of study, email. Write the data to the students.json file.
# Then write a program that creates a limited.json file with the copy of the list of students, limited to data:
# first name, last name, student id.

import json

with open("students.json", encoding="utf-8") as file, open("limited.json", "w") as limited_json:
    x = json.load(file)

    i = 0
    for student in x:
        x[i].pop("gender")
        x[i].pop("age") 
        x[i].pop("year_of_study")
        x[i].pop("email")
        print(x[i])
        i+=1
    print(x)
    
    json.dump(x, limited_json, ensure_ascii=False, indent=4)
