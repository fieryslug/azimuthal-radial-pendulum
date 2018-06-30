import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from drawnow import drawnow

SIN = math.sin
COS = math.cos
PI = math.pi



def solve3(eq0, eq1, eq2):

    delta = det3(eq0[:3], eq1[:3], eq2[:3])
    deltax = det3([eq0[3], eq0[1], eq0[2]], [eq1[3], eq1[1], eq1[2]], [eq2[3], eq2[1], eq2[2]])
    deltay = det3([eq0[0], eq0[3], eq0[2]], [eq1[0], eq1[3], eq1[2]], [eq2[0], eq2[3], eq2[2]])
    deltaz = det3([eq0[0], eq0[1], eq0[3]], [eq1[0], eq1[1], eq1[3]], [eq2[0], eq2[1], eq2[3]])

    if delta == 0:
        return

    return [deltax / delta, deltay / delta, deltaz / delta]


def det3(col0, col1, col2):
    temp0 = col0[0] * (col1[1] * col2[2] - col1[2] * col2[1])
    temp1 = col0[1] * (col1[2] * col2[0] - col1[0] * col2[2])
    temp2 = col0[2] * (col1[0] * col2[1] - col1[1] * col2[0])

    return temp0 + temp1 + temp2


def make_fig():
    plt.scatter(xplot, yplot, s=0.5, color='brown')
    plt.xlabel('t=' + '{0:.4}'.format(t))
    #ax.scatter(xplot, yplot, zplot)


r = 0.2
L = 0.4
M = 0.05
m = 0.05
g = 9.806
k = 100

t = 0
increment = 0.001
totaltime = 300
counter = 0


fig = plt.figure()
plt.ion()
ax = fig.add_subplot(111, projection='3d')

plt.ion()

timeplot = []
thetaplot = []
phiplot = []
gammaplot = []

xplot = []
yplot = []
zplot = []

rodxplot = 0
rodyplot = 0

s = ', phi=80'

theta = math.pi/4
theta_ = 0
phi = math.pi/5
phi_ = 0
gamma = 0
gamma_ = 0

theta__ = 0
phi__ = 0
gamma__ = 0

while True:
    print(t)
    print(str(theta) + ', ' + str(theta_) + ', ' + str(theta__))
    if t > totaltime:
        break


    eq0 = [r, 0, L*(COS(theta)*SIN(phi)*COS(gamma)+SIN(theta)*SIN(gamma)), L*(gamma_**2)*(COS(theta)*SIN(phi)*SIN(gamma)-SIN(theta)*COS(gamma)) + r*(phi_**2)*SIN(theta)*COS(theta) + g*COS(theta)*COS(phi)]
    eq1 = [0, r*SIN(theta), L*COS(phi)*COS(gamma), -2*r*theta_*phi_*COS(theta) + L*(gamma_**2)*COS(phi)*SIN(gamma) - g*SIN(phi)]
    eq2 = [m*r*(COS(theta)*SIN(phi)*COS(gamma)+SIN(theta)*SIN(gamma)), m*r*(SIN(theta)*COS(phi)*COS(gamma)), (m+(M/3))*L, m*r*((theta_**2+phi_**2)*SIN(theta)*SIN(phi)*COS(gamma)-2*theta_*phi_*COS(theta)*COS(phi)*COS(gamma)-(theta_**2)*COS(theta)*SIN(gamma)) - k*L*gamma]

    sol = solve3(eq0, eq1, eq2)

    if sol is None:
        print('error!')
        break


    theta__ = sol[0]
    phi__ = sol[1]
    gamma__ = sol[2]

    theta_ = theta_ + increment * theta__
    theta = theta + increment * theta_

    phi_ = phi_ + increment * phi__
    phi = phi + increment * phi_

    gamma_ = gamma_ + increment * gamma__
    gamma = gamma + increment * gamma_


    if counter >= 5:
        timeplot.append(t)
        thetaplot.append(theta)
        phiplot.append(phi)
        gammaplot.append(gamma)

        xplot.append(r * COS(theta) - L*(1-COS(gamma)))
        yplot.append(r * SIN(theta) * SIN(phi) + L*SIN(gamma))
        zplot.append(-r * SIN(theta) * COS(phi))
        drawnow(make_fig)
        counter = 0

    t += increment
    counter += 1

    theta = theta % (2*PI)
    phi = phi % (2*PI)





#plt.plot(timeplot, thetaplot)
#plt.plot(timeplot, phiplot)


#plt.plot(xplot, yplot)


