def f(n):
    i = 0
    while i < n:
        if n > 5:
            x = n // 5
            return(("/" * 5 + "-")*x + "/" * (n-(5*x)))
        else:
            return("/" * n)


print(f(-4))
print(f(0))
print(f(5))
print(f(7))
print(f(11))