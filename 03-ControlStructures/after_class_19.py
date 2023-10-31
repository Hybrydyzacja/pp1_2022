dogs_age = float(input("Podaj wiek psa w ludzkich latach: "))

if dogs_age <= 2 and dogs_age > 0:
    dogs_age = int(dogs_age * 10.5)
    print(f"Wiek psa w psich latach to {dogs_age} lat")
else:
    dogs_age = dogs_age - 2
    dogs_age_above_two = int(dogs_age * 4 + 2 * 10.5)
    print(f"Wiek psa w psich latach to {dogs_age_above_two} lata")


# def f(dog_age):
#     dogs_age = dog_age

#     if dogs_age <= 2 and dogs_age > 0:
#         dogs_age = int(dogs_age * 10.5)
#         return(f"Wiek psa w psich latach to {dogs_age} lat")
#     else:
#         dogs_age = dogs_age - 2
#         dogs_age_above_two = int(dogs_age * 4 + 2 * 10.5)
#         return(f"Wiek psa w psich latach to {dogs_age_above_two}")

