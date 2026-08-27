import numpy as np

userinput = input("Please input a polynomial function, like x**2 + 3*x - 2: ")

def user_function(v):
    str_replaced_function = userinput.replace('x', 'v')
    int_replaced_function = eval(str_replaced_function)
    return (int_replaced_function)

a = -10
p = 0.1
b = a + p


while user_function(a) * user_function(b) >= 0:
    p += 0.1
    b = a + p

c = (a + b) / 2
user_function(c)

    
def bisection(a, b):
    t = 6
    tolerance = 5 * 10**(-t)

    c = (a + b) / 2
    while user_function(c) or np.abs(c - a) > tolerance:

        c = (a + b) / 2

        if user_function(c) == 0:
            return c
        if user_function(a) * user_function(c) < 0:
            b = c
        else:
            a = c

    return c


findroot = bisection(a,b)
print(findroot)