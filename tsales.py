import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import animation
import math, copy
# from random import randint
import random
import pdb

from City import City
from Tour import Tour

grid_size = 1000
number_of_cities = 48

#initalise figure
fig = plt.figure(1)
ax = plt.axes(title="TSP", xlim=(0, grid_size), ylim=(0, grid_size))

tour = Tour(number_of_cities, grid_size)
tour.generate_new_tour()
print(tour.get_total_distance())

plt.plot([t.x for t in tour.city_list],[t.y for t in tour.city_list],"ro")

# line, = ax.plot([], [], lw=2)
plt.show()



# Tweak the graph
# fig = plt.figure()
# ax = plt.axes(xlim=(0, grid_size), ylim=(0, grid_size))
# line, = ax.plot([], [], lw=2)

# plt.show()

