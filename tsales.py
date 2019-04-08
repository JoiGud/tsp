import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import animation
from random import randint

cities = [[0,0]]
#Buum til gognin (48 borgir)
for i in range(48):
  x = randint(0,1001)
  y = randint(0,1001)
  print x,y
  cities = np.concatenate((cities, [[x,y]]), axis=0)

cities

# Setjum upp grafid
fig = plt.figure()
ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000))
line, = ax.plot([], [], lw=2)

plt.show()