array = [{"country":"Laos", "population": 7572809}, 
{"country":"Irleand", "population": 5037253}, 
{"country":"Quatar", "population": 2704000}, 
{"country":"Greece", "population": 10364658}, 
{"country":"Taiwan", "population": 	23906334}]

# print(array)

# i = 0
# while i < len(array):
#     print(array[i])
#     i += 1

i = 0
while i < len(array):
    for key, value in array[i].items():
        print(value,end=" ")
    print()
    i += 1

#drukujemy sama wartosc, bez klucza