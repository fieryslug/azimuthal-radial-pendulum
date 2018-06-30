import math

r = 50
theta = math.pi/4
phi = 0.0000005

x = r * math.sin(theta) * math.cos(phi)

y = r * math.sin(theta) * math.sin(phi)

z = -r * math.cos(theta)

phi1 = math.atan(-y/z)
theta1 = math.atan(math.sqrt(y**2 + z**2)/x)

print('phi='+str(phi))
print(theta1)
print(phi1)