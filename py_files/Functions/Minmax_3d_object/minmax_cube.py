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

def cube_f(n):
    a = 1
    x = np.linspace(-1,2,n)
    y = np.linspace(-1,2,n)
    z = np.linspace(-1,2,n)

    X, Y, Z = np.meshgrid(x, y, z)
    
    cube_constraint1 = (np.abs(X) <=1) & (np.abs(Y)<= 1) & (np.abs(Z)<=1)
    
    

    min_x, max_x = find_min_max(X[cube_constraint1])
    min_y, max_y = find_min_max(Y[cube_constraint1])
    min_z, max_z = find_min_max(Z[cube_constraint1])

    min_coordinate = (min_x, min_y, min_z)
    max_coordinate = (max_x, max_y, max_z)
    
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection = '3d')

    ax.scatter(
        X[cube_constraint1],
        Y[cube_constraint1],
        Z[cube_constraint1]
    )
    np.set_printoptions(legacy = '1.25')
    ax.scatter(*min_coordinate, s=50, c='r', label=f"Min = {min_coordinate}")
    ax.scatter(*max_coordinate, s=50, c='g', label=f"Max = {max_coordinate}")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect((1,1,1))
    
    plt.legend(bbox_to_anchor=(1.1, 1.0), loc='upper right')
    plt.savefig("/Users/eduan/work/git_work/python_works/py_files/Functions/Minmax_3d_object/cube.pdf")
    plt.tight_layout()
    plt.show()

cube_f(25)
    

