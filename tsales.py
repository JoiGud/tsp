import numpy as np
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import animation
import math, copy
# from random import randint
import random
import pdb

from City import City

size_of_grid = 1000
number_of_cities = 48

# Initialize cities pool TODO: make a class of this
cities = []
for i in range(number_of_cities):
  [x,y] = random.sample(range(size_of_grid), 2)
  cities.append(City(x,y))
  # plt.plot(x,y,"or")
print(plt.get_backend())
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()



# Tweak the graph
# fig = plt.figure()
# ax = plt.axes(xlim=(0, size_of_grid), ylim=(0, size_of_grid))
# line, = ax.plot([], [], lw=2)

# plt.show()


# tour = random.sample(range(15),15);
# for temperature in numpy.logspace(0,5,num=100000)[::-1]:
#   [i,j] = sorted(random.sample(range(15),2));
#   newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:];
#   if math.exp( ( sum([ math.sqrt(sum([(cities[tour[(k+1) % 15]][d] - cities[tour[k % 15]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]) - sum([math.sqrt(sum([(cities[newTour[(k+1) % 15]][d] - cities[newTour[k % 15]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) / temperature) > random.random():
#       tour = copy.copy(newTour);
# plt.plot([cities[tour[i % 15]][0] for i in range(16)], [cities[tour[i % 15]][1] for i in range(16)], 'xb-');
# plt.show()

