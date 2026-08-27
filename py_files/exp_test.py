import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 2

x = np.linspace(-4,8, 100)

z = np.exp(-(x-a)**2/(2*b**2))

plt.plot(x,z,'-k')

plt.savefig("/Users/eduan/work/git_work/python_works/py_files/Function_fitting/simple_gaussian/gaussian.pdf")
plt.show()