import numpy as np
import matplotlib.pyplot as plt

def plot_s_sweep_version(r1=1.0, r2=1.0, st_angle_deg=30, sweep_deg=240,
                  x_01=0.0, y_01=0.0, resolution=200, ax=None, color="k"):
    

    #new -> circle = start angle + sweep angle
    st_angle1 = np.deg2rad(st_angle_deg)
    ed_angle1 = st_angle1 + np.deg2rad(sweep_deg)

    # circle 2 where circle 1 ends
    st_angle2 = ed_angle1 - np.pi
    # mirror symmetry
    ed_angle2 = st_angle1 - np.pi

    x_02 = x_01 - (r1 + r2) * np.cos(st_angle2)
    y_02 = y_01 - (r1 + r2) * np.sin(st_angle2)

    theta1 = np.linspace(st_angle1, ed_angle1, resolution)
    theta2 = np.linspace(st_angle2, ed_angle2, resolution)

    x_1 = r1 * np.cos(theta1) + x_01
    y_1 = r1 * np.sin(theta1) + y_01
    x_2 = r2 * np.cos(theta2) + x_02
    y_2 = r2 * np.sin(theta2) + y_02


    fig, ax = plt.subplots()
    ax.set_aspect("equal")

    ax.plot(x_1, y_1, color)
    ax.plot(x_2, y_2, color)

    
    all_x = np.concatenate([x_1, x_2])
    all_y = np.concatenate([y_1, y_2])
    pad_x = 0.15 * (all_x.max() - all_x.min() + 1e-9)
    pad_y = 0.15 * (all_y.max() - all_y.min() + 1e-9)
    ax.set_xlim(all_x.min() - pad_x, all_x.max() + pad_x)
    ax.set_ylim(all_y.min() - pad_y, all_y.max() + pad_y)

    return ax


ax = plot_s_sweep_version(r1=1.0, r2=2, st_angle_deg=40, sweep_deg=200)
plt.savefig("sweep_circle.pdf")