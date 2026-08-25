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

n = 20

x = np.linspace(-3,20,n)

y = linegen(x,2,-2)



A = np.zeros((n,n))
B = np.zeros((n,n))

all_slopes = []
all_intercepts = []

for i in range(n):
    Pi = (x[i],y[i])
    for j in range(i+1,n):
        Pj = (x[j],y[j])
        a,b = two_point_parameterestimation(Pi, Pj)

        all_slopes.append(a)
        all_intercepts.append(b)

mean_slope = np.mean(all_slopes)
mean_intercept = np.mean(all_intercepts)


print(mean_slope)



y_approx = mean_slope * x + mean_intercept

plt.figure()
plt.plot(x,y, 'ok')
plt.plot(x, y_approx, '-r')
plt.show()