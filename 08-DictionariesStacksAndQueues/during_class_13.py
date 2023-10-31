import json

student_dict = {
    "name": "John",
    "surname": "Black",
    "active": True,
    "best_grade": 6,
    "hobbies": ["reading", "swimming"],
    "number": {"phone": 12365, "indeks": "98745"}
}

with open("student.json", "w", encoding="utf-8") as student_json:
    json.dump(student_dict, student_json, ensure_ascii=False, indent=4)
