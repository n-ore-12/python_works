import numpy as np

userinput = input("Please input a polynomial function, like x**2 + 3*x - 2: ")

roots = []

def user_function(v):
    str_replaced_function = userinput.replace('x', 'v')
    int_replaced_function = eval(str_replaced_function)
    for r in roots:
        int_replaced_function /= (v - r)
    return int_replaced_function


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


while True:
    a = -10
    p = 0.1
    b = a + p

    while user_function(a) * user_function(b) >= 0:
        p += 0.1
        b = a + p
        if b > 10:   
            break
    if b > 10:
        break          
    findroot = bisection(a, b)
    roots.append(findroot)
    print(findroot)

print("All roots found:", roots)