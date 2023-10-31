x = int(input("Podaj pierwwszy koordynat: "))
y = int(input("Podaj drugi koordynat: "))

print(f"x = {x}")
print(f"y = {y}")

if x == 0:
    if y == 0:
        print(f"Punkt P{x,y} znajduje się w pozycji początku układu współrzędnych")
    elif y > 0:
        print(f"Punkt P{x,y} znajduje się na osi Y, powyżej początku układu wspólrzędnych)")
    else:
        print(f"Punkt P{x,y} znajduje się na osi Y, poniżej początku układu wspólrzędnych")
elif y == 0:
    if x > 0:
        print(f"Punkt P{x,y} leży na osi X, na prawo od początku układu wspólrzędnych")
    if x < 0:
        print(f"Punkt P{x,y} leży na osi X, na lewo od początku układu współrzędnych")
elif x > 0 and y > 0:
    print(f"Punkt P{x,y} leży w pierwszej ćwiartce układu współrzędnych")
elif x < 0 and y > 0:
    print(f"Punkt P{x,y} leży w drugiej ćwiartce układu współrzędnych")
elif x < 0 and y < 0:
    print(f"Punkt P{x,y} leży w trzeciej ćwiartce układu współrzędnych")
else:
    print(f"Punkt P{x,y} leży w czwartej ćwiartce układu współrzędnych")


# def f(x,y):
#     if x == 0:
#         if y == 0:
#             return(f"Punkt P{x,y} znajduje się w pozycji początku układu współrzędnych")
#         elif y > 0:
#             return(f"Punkt P{x,y} znajduje się na osi Y, powyżej początku układu wspólrzędnych)")
#         else:
#             return(f"Punkt P{x,y} znajduje się na osi Y, poniżej początku układu wspólrzędnych")
#     elif y == 0:
#         if x > 0:
#             return(f"Punkt P{x,y} leży na osi X, na prawo od początku układu wspólrzędnych")
#         if x < 0:
#             return(f"Punkt P{x,y} leży na osi X, na lewo od początku układu współrzędnych")
#     elif x > 0 and y > 0:
#         return(f"Punkt P{x,y} leży w pierwszej ćwiartce układu współrzędnych")
#     elif x < 0 and y > 0:
#         return(f"Punkt P{x,y} leży w drugiej ćwiartce układu współrzędnych")
#     elif x < 0 and y < 0:
#         return(f"Punkt P{x,y} leży w trzeciej ćwiartce układu współrzędnych")
#     else:
#         return(f"Punkt P{x,y} leży w czwartej ćwiartce układu współrzędnych")
   