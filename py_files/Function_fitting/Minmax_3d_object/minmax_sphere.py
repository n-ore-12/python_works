import numpy as np
import matplotlib.pyplot as plt


def find_min_max(array):
    minimum = array[0]
    maximum = array[0]
    for value in array:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    return minimum, maximum

def sphere_f(R, n):
    x = np.linspace(-R,R,n)
    y = np.linspace(-R,R,n)
    z = np.linspace(-R,R,n)

    X, Y, Z = np.meshgrid(x,y,z,indexing='ij')

    sphere = X**2 + Y**2 + Z**2 <= R**2

    values = np.sqrt(X**2+Y**2+Z**2)

    values[~sphere] = np.nan


    inside_sphere = values[sphere]


    result_min, result_max = find_min_max(inside_sphere)

    print("Minimum value:", result_min, ',' , "Maximum Value:", result_max)


    fig = plt.figure()

    ax = fig.add_subplot(111,projection = '3d')

    ax.scatter(
        X[sphere], 
        Y[sphere], 
        Z[sphere], 
        s=1
    )
    ax.set_box_aspect([1, 1, 1])
    ax.set_title(f"Minimum value: {result_min}, Maximum value: {result_max}")

    plt.show()



sphere_f(1,27)

        


