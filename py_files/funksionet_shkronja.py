import numpy as np 
import matplotlib.pyplot as plt

r1 = 1.0
r2 = 1.0
st_angle1 = np.deg2rad(30)
ed_angle1= np.deg2rad(270)
#ed_angle2 = np.deg2rad(-150)
#st_angle2 = np.arcsin((r1/r2)*np.sin(ed_angle1))
x_01, y_01 = 0, 0
resolution = 200

st_angle2 = ed_angle1 - np.pi

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
ax.plot(x_1,y_1,"k")
ax.plot(x_2,y_2, "k")


plt.ylim(-4,4)
plt.xlim(-3,3)

ax.set_aspect("equal")
plt.savefig("/Users/eduan/work/git_work/python_works/pythoncircle.pdf")
print(np.rad2deg(st_angle2))
