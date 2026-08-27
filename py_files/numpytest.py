import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
a = np.array([[2,4,5], [3,7,1]])

b = np.array([[[1,2],[2,6]],
              [[3,7],[4,9]]])

print(len(a))
print(b.shape)

u = np.linspace(0,21,4)
print(u)

l = np.zeros((4,3))
m = np.ones((4,3))
n = np.eye(4)
print(l)
print()
print(m)
print()
print(n)

o = rng.integers(1,10, 10, endpoint=True)
p = rng.standard_normal(size=100000)

print(o)

j = np.arange(1,6)
print(j)
x = np.arange(-5,0)
print(x)
z = np.arange(2,9,2)
print(z)
c = np.linspace(0,10,15)
print(c)
# plt.figure()
# plt.hist(p, bins=100, color="k", density=False, histtype="step")
# plt.show()

# plt.figure()
# image = rng.random((10,20))
# plt.imshow(image, cmap=plt.cm.hot)
# plt.colorbar()
# plt.show()

t = np.array([1,3,4,9,10,22,34,123])

print(t[:-1])

# y = np.diag(np.arange(4))
# y[3,2] = 191
# print(y)

# w = np.linspace(14,0,15)
# q = np.linspace(0,11,12)
# w[4::] = q[2:11:2]
# print(w)


arr = np.ones((4,4))
arr[3,1] = 6
arr[2,3] = 2

arr1 = np.diag(np.arange(2,7).reshape([6,5]), k=-1)
print(arr1)