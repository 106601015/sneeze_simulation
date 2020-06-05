
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math
#constant
g=9.8 #m/s**2

#time remain
tgo=0 #s
tend=2 #s
cut=30

#fire initial velocity and angle and height
V0=30 #m/s                                  #################
theta=10*(math.pi/180) #angle(do)           ###########
u0=V0*math.cos(theta) #m/s
v0=0
w0=V0*math.sin(theta) #m/s
height=5 #m

#calculate drop base data
r=16/10**6 #m                               ########
volume=(4/3)*math.pi*r**3
mass=volume
print('mass:',mass)

#calculate air resistance(0=mg-fd, fd =0.5* zo * v**2 * cd * a)
zo=1.293 #kg/m**3
cd=0.47 #circle air resistance constant
a=r*r*math.pi #m**2, area
fd=0.5*zo*V0**2*cd*a #kg*m/s
print('fd',fd)

print('final v=',(2*mass*g/zo/a/cd)**0.5) #!!!!!!

road=[]
fig = plt.figure()
ax = plt.axes(projection="3d")
'''
ax.set_xlim3d(0, 70)
ax.set_ylim3d(0,1)
ax.set_zlim3d(-5,8)
'''
del_t = np.linspace(tgo, tend, cut)
x_line = np.multiply(u0, del_t)
z_line = np.add(np.add(height, np.subtract(0, np.divide(np.multiply(np.power(del_t, 2), g), 2))), np.multiply(del_t, w0))
for i in range(10):
    y_line = np.linspace(float(i/10), float(i/10), cut)
    road.append(ax.plot3D(x_line, y_line, z_line, 'b'))

plt.show()
