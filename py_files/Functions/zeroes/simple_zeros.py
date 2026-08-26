import numpy as np
import re 
import matplotlib.pyplot as plt

user_input = input("Please enter a quadratic in factored or standard form: ")

def quadratic_unfactored(user_input):
    a_b_c_pattern = r"([+-]?\d*)x\^2\s*([+-]?\d*)x\s*([+-]?\d+)"

    match = re.fullmatch(a_b_c_pattern, user_input.replace(" ",""))

    if match:
        a = match.group(1)
        b = match.group(2)
        c = match.group(3)

        if a == 0:
            print("Value of 'a' cannot be 0.")
        elif a == "":
            a = 1
        elif a == "-":
            a = -1
        else:
            a = int(a)

        if b == "":
            b = 1
        elif b == '-':
            b = -1
        else:
            b = int(b)

        c = int(c)

        delta = b**2 - 4*a*c

        zero1 = (-b + np.sqrt(delta)) / (2*a)
        zero2 = (-b - np.sqrt(delta)) / (2*a)
        print(a, b, c)
        print('The roots are:', zero1, zero2)
    else:
        print("Invalid format.")

def quadratic_factored(user_input):
    pattern = r'[+-]\d+'
    numbers = re.findall(pattern, user_input)
    zero1 = -(int(numbers[0]))
    zero2 = -(int(numbers[1]))
    print('The roots are:', zero1, zero2)




if '^' in user_input:
    quadratic_unfactored(user_input)
else:
    quadratic_factored(user_input)







    