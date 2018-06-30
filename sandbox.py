
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


print(solve([1, 2, 3, 15], [3550, 238, 777, -1351], [1381683.1135, -1231211088, 20.88, 80000]))
