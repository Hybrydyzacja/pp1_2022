
# def f(plusminus):
#     # x = '++++-----'
#     y = plusminus.count('+')
#     return(y)

# print(f("++++--"))


# def fibb(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a

# print(fibb(6))

# def Fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)

# print(Fibonacci(6))                                           


def fibonacci_numbers(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)
 
 
n = 7
for i in range(0, n):
    print(fibonacci_numbers(i), end=" ")