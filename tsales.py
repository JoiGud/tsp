import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import animation
import math, copy
# from random import randint
import random
import pdb

from city import City
from tour import Tour

# Calculate the acceptance probability
def acceptance_probability(energy, new_energy, current_temp):
    # Accept the new solution if it's better
    if (new_energy < energy):
        return 1.0;
    # Calculate an acceptance probability if the new solution is worse.
    return math.exp((energy - new_energy) / current_temp)

grid_size = 1000
number_of_cities = 48
temperature = 10000
cooling_rate = 0.003

# Initalize starting values
current_tour = Tour(number_of_cities, grid_size)
current_tour.init_city_list()
current_tour.init_tour_list()
best_solution = copy.deepcopy(current_tour)

distance_timeseries = [best_solution.get_total_distance()]

print("Initial tour distance: "+str(best_solution.get_total_distance()))

# Initalize figure and plot the points
fig1 = plt.figure(1)
ax = plt.axes(title="TSP", xlim=(0, grid_size), ylim=(0, grid_size))
plt.plot([t.x for t in best_solution.city_list],[t.y for t in best_solution.city_list],"ro")

# Lets do some annealing
while temperature > 1:
  # The consecutive-swap neighbour generator is expected to perform better than the arbitrary-swap one
  [i,k] = random.sample(range(number_of_cities),2)
  new_tour = current_tour.get_new_tour_with_swapped_cities(i,k)

  if(acceptance_probability(current_tour.get_total_distance(), new_tour.get_total_distance(), temperature) > random.uniform(0,1)):
    current_tour = copy.copy(new_tour)

  if(current_tour.get_total_distance() < best_solution.get_total_distance()):
    best_solution = copy.copy(current_tour)

  distance_timeseries.append(best_solution.get_total_distance())

  temperature *= 1-cooling_rate

print("Final tour distance: "+str(best_solution.get_total_distance()))

plt.plot([t.x for t in best_solution.tour_list],[t.y for t in best_solution.tour_list],"b")
plt.plot([t.x for t in [best_solution.tour_list[-1], best_solution.tour_list[0]]],\
  [t.y for t in [best_solution.tour_list[-1], best_solution.tour_list[0]]],"b")

plt.show()

fig2 = plt.figure(2)
plt.plot(distance_timeseries,'.')
plt.show()
