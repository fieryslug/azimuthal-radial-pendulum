import math
import matplotlib.pyplot as plt

def solve2(eq0, eq1):

    delt0 = det2([eq0[0], eq0[1]], [eq1[0], eq1[1]])

    if delt0 == 0:
        return

    deltx = det2([eq0[2], eq0[1]], [eq1[2], eq1[1]])
    delty = det2([eq0[0], eq0[2]], [eq1[0], eq1[2]])

    return[deltx / delt0, delty / delt0]



def det2(col0, col1):
    return col0[0] * col1[1] - col0[1] * col1[0]

theta = math.pi / 2.2
theta_ = 0
delta = 0
delta_ = 0

theta__ = 0
delta__ = 0

t = 0
increment = 0.00001
totaltime = 20
timeplot = []
thetaplot = []
deltaplot = []
theta_plot = []
delta_plot = []

r = 0.5
m = 0.05
M = 0.005
k = 10
g = 9.806


while t <= totaltime:

    print('t=' + str(t) + ', ' + str(theta))
    eq0 = [r, math.cos(theta), -g*math.sin(theta)]
    eq1 = [m*r*math.cos(theta), M+m, -k*delta + m*r*(theta_**2)*math.sin(theta)]

    sol = solve2(eq0, eq1)
    if sol is None:
        print('error!')
        break

    theta__ = sol[0]
    delta__ = sol[1]

    theta_ = theta_ + increment * theta__
    theta = theta + increment * theta_

    delta_ = delta_ + increment * delta__
    delta = delta + increment * delta_

    timeplot.append(t)
    thetaplot.append(theta)
    theta_plot.append(theta_)
    deltaplot.append(delta)
    delta_plot.append(delta_)

    t += increment


#plt.plot(timeplot, deltaplot)
plt.plot(timeplot, theta_plot)
#plt.plot(timeplot, phi_plot)
plt.xlabel('k=' + str(k))
plt.show()


