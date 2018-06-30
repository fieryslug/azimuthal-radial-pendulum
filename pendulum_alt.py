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
    plt.scatter(xplot, yplot, s=0.5)
    plt.xlabel('r=' + str(r) + ', M=' + str(M) + ', m=' + str(m) + ', k=' + str(k))
    #ax.scatter(xplot, yplot, zplot)


r = 0.2
M = 0.016666
m = 0.05
g = 9.806
k = 100

t = 0
increment = 0.0001
totaltime = 300
counter = 0


fig = plt.figure()
plt.ion()
ax = fig.add_subplot(111, projection='3d')

plt.ion()

timeplot = []
thetaplot = []
phiplot = []
deltaplot = []
xplot = []
yplot = []
zplot = []

theta = PI / 4
theta_ = 0
phi = 0
phi_ = 0.01
delta = 0
delta_ = 0

theta__ = 0
phi__ = 0
delta__ = 0

while True:
    print(t)
    print(str(theta) + ', ' + str(theta_) + ', ' + str(theta__))
    if t > totaltime:
        break


    eq0 = [r, 0, COS(theta)*SIN(phi), r*(phi_**2)*SIN(theta)*COS(theta) + g*COS(theta)*COS(phi)]
    eq1 = [0, r*SIN(theta), COS(phi), -2*r*theta_*phi_*COS(theta) - g*SIN(phi)]
    eq2 = [m*r*COS(theta)*SIN(phi), m*r*SIN(theta)*COS(phi), M+m, m*r*(theta_**2 + phi_**2)*SIN(theta)*SIN(phi) - 2*m*r*theta_*phi_*COS(theta)*COS(phi) - k*delta]

    sol = solve3(eq0, eq1, eq2)

    if sol is None:
        print('error!')
        break


    theta__ = sol[0]
    phi__ = sol[1]
    delta__ = sol[2]

    theta_ = theta_ + increment * theta__
    theta = theta + increment * theta_

    phi_ = phi_ + increment * phi__
    phi = phi + increment * phi_

    delta_ = delta_ + increment * delta__
    delta = delta + increment * delta_

    if counter >= 50:
        timeplot.append(t)
        thetaplot.append(theta)
        phiplot.append(phi)
        deltaplot.append(delta)
        xplot.append(r * COS(theta))
        yplot.append(r * SIN(theta) * SIN(phi) + delta)
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

