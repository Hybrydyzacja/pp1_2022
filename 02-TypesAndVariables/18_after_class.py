a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

p = (a+b+c)/2
area = ((p*(p-a)*(p-b)*(p-c))**0.5)
print(area)
