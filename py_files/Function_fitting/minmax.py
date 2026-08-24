import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()

def minimum_list(a):
    min_l = a[0]
    for i in range(len(a)):
        if min_l > a[i]:
            min_l = a[i]
    return min_l



def maximum_list(a):
    max_l = a[0]
    for i in range(len(a)):
        if max_l < a[i]:
            max_l = a[i]

    return max_l

# lower = rng.integers(-5,0,1)
# upper = rng.integers(1,10,1)
# size = rng.integers(10,20,1)
# a = rng.integers(lower,upper,size)
# print(a)

# print(minimum_list(a))
# print(maximum_list(a))

n = 400
x = np.linspace(-5,6,n)
y = -(x+1)*(x-2)

print(minimum_list(y))
print(maximum_list(y))
plt.plot(x,y,'.k')
#plt.plot(0.5,-2.25,'or')
plt.axhline(y=0)
plt.show()
