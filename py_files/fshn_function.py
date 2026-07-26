import numpy as np 
import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))


def func_f(color="b", resolution=200):
    y = np.linspace(0, 4, resolution)
    plt.plot(np.full_like(y, 0.5), y, color)

    x = np.linspace(0.5, 3, resolution)
    plt.plot(x, np.full_like(x, 4), color)

    x = np.linspace(0.5, 3, resolution)
    plt.plot(x, np.full_like(x, 2.5), color)



def func_s(color="y", resolution=200):
    #upper semicircle
    theta = np.linspace(np.pi/2, 3*np.pi/2, resolution)
    x = 4.5 + np.cos(theta)
    y = 3 + np.sin(theta)
    plt.plot(x, y, color)

    #lower semicircle
    theta = np.linspace(-np.pi/2, np.pi/2, resolution)
    x = 4.5 + np.cos(theta)
    y = 1 + np.sin(theta)
    plt.plot(x, y, color)

    #top left  S 
    theta = np.linspace(0, np.pi, resolution)
    x = 4.5 - np.cos(theta)
    y = 3 + np.sin(theta)
    plt.plot(x, y, color)

    #bottom right  S
    theta = np.linspace(np.pi, 2*np.pi, resolution)
    x = 4.5 + np.cos(theta)
    y = 1 + np.sin(theta)
    plt.plot(x, y, color)



def func_h(color="r", resolution=200):
    y = np.linspace(0,4,resolution)
    plt.plot(np.full_like(y,6), y, color)
    plt.plot(np.full_like(y,8.5), y, color)

    x = np.linspace(6, 8.5, resolution)
    plt.plot(x, np.full_like(x, 2), color)



def func_n(color="g", resolution=200):
    y = np.linspace(0, 4, resolution)
    plt.plot(np.full_like(y, 9.5), y, color)
    plt.plot(np.full_like(y, 12), y, color)

    x = np.linspace(9.5, 12, resolution)
    y = -1.6*x + 19.2
    plt.plot(x, y, color)


##format


plt.xlim(0,13)
plt.ylim(-0.5,4.5)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Fakulteti i Shkencave Natyrore")

func_f(color="b", resolution=200)
func_s(color="y", resolution=200)
func_h(color="r", resolution=200)
func_n(color="g", resolution=200)

plt.savefig("/Users/eduan/work/git_work/python_works/FSHN_new.pdf")

plt.show
