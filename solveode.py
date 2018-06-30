
import math
import matplotlib.pyplot as plt

COS = math.cos
SIN = math.sin

PI = math.pi

def solve(eq0, eq1, eq2):

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


r = 0.5
k = 1000
m = 0.05
M = 0.05
g =  9.80655

theta = PI/4
theta_ = 0
phi = PI/3
phi_ = 1
delta = 0
delta_ = 0

theta__ = 0
phi__ = 0
delta__ = 0

timeplot = []
thetaplot = []
phiplot = []
deltaplot = []

increment = 0.00001

totaltime = 2
t = 0
counter = 0

while True:
    print('iterate' + str(t))
    print(delta)

    if t > totaltime:
        break

    eq0 = [r, 0, COS(theta) * SIN(phi), r * (phi_ ** 2) * COS(theta) * SIN(theta) - g * SIN(theta)]
    eq1 = [0, r * SIN(theta), COS(phi), -2 * r * phi_ * theta_ * COS(theta)]
    eq2 = [m * r * COS(theta) * SIN(phi), m * r * SIN(theta) * COS(phi), M + m, -k * delta + m * r * (theta_ ** 2) * SIN(theta) * SIN(phi) - 2 * m * r * theta_ * phi_ * COS(theta) * COS(phi) + r * (phi_ ** 2) * SIN(theta) * SIN(phi)]

    tup = solve(eq0, eq1, eq2)

    if tup is None:
        print('error!!!')
        break

    theta__ = tup[0]
    phi__ = tup[1]
    delta__ = tup[2]

    theta = theta + theta_ * increment
    theta_ = theta_ + theta__ * increment

    phi_ = phi_ + phi__ * increment
    phi = phi + phi_ * increment

    delta_ = delta_ + delta__ * increment
    delta = delta + delta_ * increment


    #theta = theta % (2*PI)
    #phi = phi % (2*PI)

    if counter == 100:
        counter = 0
        timeplot.append(t)
        thetaplot.append(theta)
        phiplot.append(phi)
        deltaplot.append(delta)

    t += increment
    counter += 1


xplot = []
yplot = []

for i in range(len(thetaplot)):
    xplot.append(r * SIN(thetaplot[i]) * COS(phiplot[i]))
    yplot.append(r * SIN(thetaplot[i]) * SIN(phiplot[i]))

plt.plot(xplot, yplot)
#plt.plot(timeplot, thetaplot)
#plt.plot(timeplot, phiplot)
plt.show()




