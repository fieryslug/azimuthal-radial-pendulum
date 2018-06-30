import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from drawnow import drawnow

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

def make_fig():
    plt.scatter(xplot, yplot, s = 0.5)
    #ax.scatter(xplot, yplot, zplot)

r = 0.5
g = 9.806

theta = math.pi / 8
theta_ = 0
phi = math.pi / 4
phi_ = 3

theta__ = 0
phi__ = 0

t = 0
increment = 0.0001
totaltime = 100
fig = plt.figure()
plt.ion()

counter = 0
timeplot = []
thetaplot = []
phiplot = []
xplot = []
yplot = []
zplot = []

while True:
    if t > totaltime:
        break

    theta__ = (r * (phi_ ** 2) * math.sin(theta) * math.cos(theta) - g * math.sin(theta)) / r
    phi__ = - (2 * phi_ * theta_ * math.cos(theta)) / (math.sin(theta))

    theta_ = theta_ + increment * theta__
    theta = theta + increment * theta_

    phi_ = phi_ + increment * phi__
    phi = phi + increment * phi_

    #theta = theta % (2 * math.pi)
    phi = phi % (2 * math.pi)

    print(phi_)

    if counter == 100:
        timeplot.append(t)
        thetaplot.append(theta)
        phiplot.append(phi)
        xplot.append(r * math.sin(theta) * math.cos(phi))
        yplot.append(r * math.sin(theta) * math.sin(phi))
        zplot.append(-r * math.cos(theta))
        drawnow(make_fig)
        counter = 0


    t += increment
    counter += 1





#.plot(timeplot, thetaplot)
#plt.plot(timeplot, phiplot)
#plt.plot(xplot, yplot)
#plt.show()