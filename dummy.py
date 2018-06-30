import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# function that returns dy/dt
def model(y, t):
    k = 0.3
    dydt2 = -y
    return dydt2



# initial condition
y0 = 5

# time points
t = np.linspace(0,20)

# solve ODE
y = odeint(model,y0,t)


# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()