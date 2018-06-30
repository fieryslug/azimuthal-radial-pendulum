import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from drawnow import drawnow
import json

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




def main(rd=0.2, Le=0.4, Ma=0.05, ma=0.05, gr=9.806, kx=.0, th=math.pi/4, ph=math.pi/4, max=60, T=1.0):

    r = rd
    L = Le
    M = Ma
    m = ma
    g = gr
    k = kx

    t = 0
    increment = 0.00001
    totaltime = max
    counter = 0

    timeplot = []
    thetaplot = []
    phiplot = []
    gammaplot = []

    xplot = []
    xregplot = []
    yplot = []
    yregplot = []
    zplot = []

    rodxplot = 0
    rodyplot = 0

    s = ', phi=80'

    theta = th
    theta_ = 0
    phi = ph
    phi_ = 0
    gamma = 0
    gamma_ = 0

    theta__ = 0
    phi__ = 0
    gamma__ = 0

    while True:
        print(t)
        #print(str(theta) + ', ' + str(theta_) + ', ' + str(theta__))
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


        if counter >= 100:
            timeplot.append(t)
            thetaplot.append(theta)
            phiplot.append(phi)
            gammaplot.append(gamma)

            xplot.append(r * COS(theta) - L*(1-COS(gamma)))
            xregplot.append((r * COS(theta) - L*(1-COS(gamma)))/COS(2*PI*t/T))
            yplot.append(r * SIN(theta) * SIN(phi) + L*SIN(gamma))
            yregplot.append((r * SIN(theta) * SIN(phi) + L*SIN(gamma))/SIN(2*PI*t/T))
            zplot.append(-r * SIN(theta) * COS(phi))
            #drawnow(make_fig)
            counter = 0

        t += increment
        counter += 1

        theta = theta % (2*PI)
        phi = phi % (2*PI)

    dat = []
    for index in range(len(timeplot)):
        dat.append(
            {'t': timeplot[index], 'x': xplot[index], 'y': yplot[index], 'z': zplot[index], 'theta': thetaplot[index],
             'phi': phiplot[index], 'gamma': gammaplot[index]})

    with open('pona.json', 'w') as f:
        json.dump(dat, f, indent=4)


    #plt.plot(timeplot, xplot)
    #plt.plot(timeplot, yplot)
    plt.plot(xplot, yplot)
    plt.xlabel('r=' + str(r) + ', L=' + str(L) + ', M=' + str(M) + ', m=' + str(m) + ', k=' + str(k))
    #plt.plot(xplot, yplot)
    plt.show()






    #plt.plot(timeplot, thetaplot)
    #plt.plot(timeplot, phiplot)


    #plt.plot(xplot, yplot)


def convert(theta, phi):
    r = 50

    x = r * math.sin(theta) * math.cos(phi)

    y = r * math.sin(theta) * math.sin(phi)

    z = -r * math.cos(theta)

    phi1 = math.atan(-y / z)
    theta1 = math.atan(math.sqrt(y * 2 + z * 2) / x)

    return [theta1, phi1]


if __name__ == '__main__':
    #phi = float(input('phi_0: '))
    phi = 1e-3

    mM = float(input('M: '))

    tot = int(input('max: '))
    ang = convert(math.pi/4, phi)

    plt.ylabel('phi= ' + str(phi))

    main(th=ang[0], ph=ang[1], max=tot, kx=200, Ma = mM)
