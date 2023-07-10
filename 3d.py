from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

alpha = 15.6
beta = 28
R = -1.143
C_2 = -0.714

def chua(u,t):
  x, y, z = u
  f_x = C_2*x + 0.5*(R-C_2)*(abs(x+1)-abs(x-1))
  return [alpha*(y-x-f_x), x - y + z, -beta * y]

t_0 = 0
dt = 0.02
t_final = 100
t = np.arange(t_0, t_final, dt)
u0 = [0.7,0,0]
sol ,info = odeint(chua, u0, t,full_output=1)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(sol[:,0], sol[:,1], sol[:,2], 'blue')
ax.set_xlabel('x (V)')
ax.set_ylabel('y (V)')
ax.set_zlabel('z (V)')
plt.show()
