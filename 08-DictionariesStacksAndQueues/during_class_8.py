
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}


print(person)
print(person["name"])
print(person["hobby"])

person["surname"] = "Nowak"
print(person)

person["married"] = False
print(person)

person["gender"] = "male"
print(person)

person["hobby"] += ["bicycle"]
print(person)

# person["hobby"].append("bicycle")    #można tez tak
# print(person)


person["phone"]["work"] = "313131444"
print(person)
# 1) identyfikator slownika person["phone"]
# 2) klucz ze słownika ["word"]
# jezeli identyfikator/klucz bedzie juz obecna w slowniku, to bedzie podmianka,
# jezeli nie - wartosc zostanie dodana




# phone = {
# 	"Product":"Mobile",
# 	"Model": "XUT",
# 	"Units": 120,
# 	"Available": True
# }

# for i in phone:
#     item = phone.items()
#     print(item)
#     break
# print()
# for i in phone.items():
#     print(item)
#     break
