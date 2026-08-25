import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,100)
y = np.linspace(-3,3,100)

X,Y = np.meshgrid(x,y)

Z = Y**2 - X**2

zeros = np.isclose(Z,0, rtol=0.00000001)

x_zero = X[zeros] # because x_zero = y_zero we dont need y_zero



fig = plt.figure(figsize=((8,6)))
ax = fig.add_subplot(111,projection='3d')

ax.plot_surface(X,Y,Z ,cmap = 'cool',edgecolor='None', alpha=0.5)

print(len(x_zero))

ax.plot(x_zero,x_zero, np.zeros_like(x_zero), '-r', lw=2, alpha=1, label=r'$z = 0, y = \pm x$')
ax.plot(x_zero,-x_zero, np.zeros_like(x_zero), '-r', lw=2)
plt.legend()
ax.set_xlabel("X", color='k')
ax.set_ylabel("Y", color='k')
ax.set_zlabel("Z", color='k')

plt.title(r'Finding the zeroes of the function $z = y^2 - x^2$')

fig.savefig("/Users/eduan/work/git_work/python_works/py_files/Function_fitting/zeroes/saddle_function.pdf")

plt.show()
