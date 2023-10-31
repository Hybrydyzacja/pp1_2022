def f(human_age):

    if human_age >= 2:
        age = 2*10 + ((human_age-2) *4)
        return(age)
    else:
        age = human_age *10
        return(age)

print(f(15))