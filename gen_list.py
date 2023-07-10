import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

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
t_final = 160000
t = np.arange(t_0, t_final, dt)
u0 = [0.7,0,0]

import struct

def float_to_bin(num):
  return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def bin_to_float(binary):
  return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

sol = odeint(chua, u0, t)
s = [int(float_to_bin(sol[:,0][i])[10:]+float_to_bin(sol[:,1][i])[11:]+float_to_bin(sol[:,2][i])[11:],2) for i in range(0,len(sol[:,2]),200)]
with open("data.bin","wb") as file:
  b = bytes()
  file.write(b.join((struct.pack("Q",elem) for elem in s)))
  file.close()
