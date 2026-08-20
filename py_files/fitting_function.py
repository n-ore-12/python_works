import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

def linegen(x, a, b):
    e = rng.normal(loc = 0, scale=1, size=len(x))
    return a*x + b + e

def two_point_parameterestimation(p1,p2):
    a = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - a*p1[0]
    return a, b

def multipoint_parameter_1(x,y):
    all_slopes = []
    all_intercepts = []
    for i in range(len(x) - 1):
        a,b = two_point_parameterestimation((x[i],y[i]),(x[i+1],y[i+1]))
        all_slopes.append(a)
        all_intercepts.append(b)

    estimation_slope = np.mean(all_slopes)
    estimation_intercept = np.mean(all_intercepts)

    return estimation_slope, estimation_intercept
    
def multipoint_parameter_2(x,y):
    all_slopes = []
    all_intercepts = []

    for i in range(0, len(x) - 2, 2):
        a,b = two_point_parameterestimation((x[i],y[i]),(x[i+2],y[i+2]))
        all_slopes.append(a)
        all_intercepts.append(b)

    if len(x) % 2 == 0:
        a,b = two_point_parameterestimation((x[-1],y[-1]),(x[-2],y[-2]))
        all_slopes.append(a)
        all_intercepts.append(b) 

    a, b = two_point_parameterestimation((x[0],y[0]),(x[-1],y[-1]))
    all_slopes.append(a)
    all_intercepts.append(b)

    estimation_slope = np.mean(all_slopes)
    estimation_intercept = np.mean(all_intercepts)
    
    return estimation_slope, estimation_intercept

def multipoint_parameter_3(x,y):
    all_slopes = []
    all_intercepts = []

    for i in range(0, len(x) - 3, 3):
        a,b = two_point_parameterestimation((x[i],y[i]),(x[i+3],y[i+3]))
        all_slopes.append(a)
        all_intercepts.append(b)

    if len(x) % 3 == 0:
        a,b = two_point_parameterestimation((x[-1],y[-1]),(x[-3],y[-3]))
        all_slopes.append(a)
        all_intercepts.append(b) 

    a, b = two_point_parameterestimation((x[0],y[0]),(x[-1],y[-1]))
    all_slopes.append(a)
    all_intercepts.append(b)

    estimation_slope = np.mean(all_slopes)
    estimation_intercept = np.mean(all_intercepts)
    
    return estimation_slope, estimation_intercept

def multipoint_parameter_n(x,y,n):

    all_slopes = []
    all_intercepts = []

    for i in range(1, len(x) - n, n):
        a,b = two_point_parameterestimation((x[i],y[i]),(x[i+n],y[i+n]))
        all_slopes.append(a)
        all_intercepts.append(b)

    last_point_used = ((len(x)-1) // n) * n

    if last_point_used != (len(x)-1):
        a,b = two_point_parameterestimation((x[-1],y[-1]),(x[last_point_used],y[last_point_used]))
        all_slopes.append(a)
        all_intercepts.append(b) 
    if len(x) <= 10:
        a, b = two_point_parameterestimation((x[0],y[0]),(x[-1],y[-1]))
        all_slopes.append(a)
        all_intercepts.append(b)

    estimation_slope = np.mean(all_slopes)
    estimation_intercept = np.mean(all_intercepts)
    
    return estimation_slope, estimation_intercept




N = 100
x = np.linspace(-25,75,N)
a = 2
b = -2

y = linegen(x,2,-2)

N_exp = 50
multipoint_exp = np.zeros(N_exp)

for i in range(1, N_exp):
    multipoint_exp[i], _ = multipoint_parameter_n(x,y,i)


print("Using first and last points:",two_point_parameterestimation((x[0],y[0]),(x[-1],y[-1])))

print("Finding slope from every consecutive point:",multipoint_parameter_1(x,y))

print("Finding slope from every two points:", multipoint_parameter_2(x,y))

print("Finding slope from every three points:", multipoint_parameter_3(x,y))

print("Finding slope from every n points:", multipoint_parameter_n(x,y,N-1))

plt.figure()
plt.plot(x,y, 'ok')
plt.plot([x[0],x[-1]], [y[0], y[-1]], '-r')

plt.figure()
plt.plot(range(N_exp),multipoint_exp, 'ok')
plt.xlabel("Step size (n)")
plt.ylabel("Estimated slope")

plt.show()