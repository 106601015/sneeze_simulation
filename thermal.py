
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math
#constant
g=9.8 #m/s**2

def drop_plot():
    #time remain
    tgo=0 #s
    tend=2 #s
    cut=30

    #fire initial velocity and angle and height
    V0=177000/3600 #m/s                                ###
    theta=0*(math.pi/180) #angle(do)                   ###
    u0=V0*math.cos(theta) #m/s
    v0=0
    w0=V0*math.sin(theta) #m/s
    height=1.8 #m

    #calculate drop base data
    r=1.6/10**6 #m                                     ###
    volume=(4/3)*math.pi*r**3
    mass=volume

    #calculate air resistance(0=mg-fd, fd =0.5* zo * v**2 * cd * a)
    zo=1.293 #kg/m**3
    cd=0.47 #circle air resistance constant
    a=r*r*math.pi #m**2, area
    fd=0.5*zo*V0**2*cd*a #kg*m/s
    vend=(8*r*g/3/zo/cd)**0.5

    print('for r=', r, 'final v=', vend) #!!!!!!

    road=[]
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.set_xlim3d(0, 10)
    ax.set_zlim3d(0,2)

    del_t = np.linspace(tgo, tend, cut)
    x_line = np.multiply(u0, del_t)
    z_line = np.add(np.add(height, np.subtract(0, np.divide(np.multiply(np.power(del_t, 2), g), 2))), np.multiply(del_t, w0))
    for i in range(10):
        y_line = np.linspace(float(i/10), float(i/10), cut)
        road.append(ax.plot3D(x_line, y_line, z_line, 'b'))

    plt.show()

u0=14 #m/s
mu=18.5/10**6
zo=1.293 #kg/m**3
fr=mu/zo *10**5

def show_parcel_horizontal():
    t,d=[],[]
    for i in range(31):
        t1=float(i/10)
        t.append(t1)
        d.append(u0/fr*(1-math.exp(-fr*t1)))
        #print('for u0=',u0, 'and t1=',t1, ', parcel u:', u0*math.exp(-fr*t1), ', parcel go to:', u0/fr*(1-math.exp(-fr*t1)))
    fig = plt.figure()
    ax = plt.axes()
    ax.plot(t, d)
    plt.show()

def cceq(T):
    return 2.53*10**11*math.exp(-5.42*1000/T)

def show_parcel_vertical():
    T=300 ###
    es=cceq(T)
    e=es*0.9 ###
    q=0.622*e/101325
    Tv=T*(1+0.62*q)
    #print('parcel:', T, 'K es=', es,', e=', e, ', q=', q, ', Tv=', Tv)
    Ta=295 ###
    esa=cceq(Ta)
    ea=esa*0.6 ###
    qa=0.622*ea/101325
    Tva=Ta*(1+0.62*qa)
    #print('around:', Ta, 'K es=', esa,', e=', ea, ', q=', qa, ', Tv=', Tva)
    a=((Tv-Tva)/Tva)*g

    t,d=[],[]
    for i in range(31):
        t1=float(i/10)
        t.append(t1)
        d.append(0.5* a *t1**2)
        #print('t1=',t1, ', parcel w:', a*t1, ', parcel go to:', 0.5* a *t1**2)
    fig = plt.figure()
    ax = plt.axes()
    ax.plot(t, d)
    plt.show()


drop_plot()
show_parcel_horizontal()
show_parcel_vertical()