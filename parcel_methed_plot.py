
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = plt.axes(projection="3d")

tgo=0 #s
tend=2 #s
g=9.8 #m/s**2
V0=30 #m/s
theta=10*(math.pi/180) #do
u=V0*math.cos(theta) #m/s
v=V0*math.sin(theta) #m/s
print(V0,theta,u,v)
w=0 #m/s
height=5 #m
point=30

del_t = np.linspace(tgo, tend, point)
x_line = np.multiply(u, del_t)
y_line = np.linspace(0, 0, point)
z_line = np.add(np.add(height, np.subtract(0, np.divide(np.multiply(np.power(del_t, 2), g), 2))), np.multiply(del_t, v))
print(x_line, y_line, z_line)

ax.plot3D(x_line, y_line, z_line, 'gray')
plt.show()
