import math
import matplotlib.pyplot as plt

theta = math.pi/50
theta_ = 0
theta__ = 0

g = 9.806
l = 0.5

t = 0
increment = 0.0001
totaltime = 60

thetaplot = []
timeplot = []

while True:
    if t > totaltime:
        break

    theta__ = -(g/l)*math.sin(theta)

    theta_ = theta_ + increment * theta__
    theta = theta + increment * theta_

    print(theta)
    thetaplot.append(theta)
    timeplot.append(t)

    t += increment

plt.plot(timeplot, thetaplot)
plt.show()

