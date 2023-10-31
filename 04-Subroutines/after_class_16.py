def month(n):
    if n == 1:
        return("January")
    elif n == 2:
        return("Feb")
    elif n == 3:
        return("March")
    elif n == 4:
        return("April")
    elif n == 5:
        return("June")
    elif n == 6:
        return("July")
    elif n == 7:
        return("August")
    elif n == 8:
        return("January")
    elif n == 9:
        return("September")
    elif n == 10:
        return("October")
    elif n == 11:
        return("November")
    elif n == 12:
        return("December")        
    else:
        return("Zła data")

print(month(7))