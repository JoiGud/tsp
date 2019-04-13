import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import animation
import math, copy
import random

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
temperature = 100000
cooling_rate = 0.003
stopping_temperature = 1e-4
stopping_iter = 100000
iteration_number = 1

# Initalize starting values
current_tour = Tour(number_of_cities, grid_size)
current_tour.init_city_list()
current_tour.init_tour_list()
best_solution = copy.deepcopy(current_tour)

distance_timeseries = [best_solution.tour_distance]
solution_timeseries = [best_solution.tour_list]

print("Initial tour distance: "+str(best_solution.tour_distance))

# Initalize figure and plot the points
fig1 = plt.figure(1)
ax = plt.axes(title="TSP", xlim=(0, grid_size), ylim=(0, grid_size))
plt.plot([t.x for t in best_solution.city_list],[t.y for t in best_solution.city_list],"ro")

# Set up animate object
solution_evolving, = ax.plot([], [], lw=2)

# Lets do some annealing
while temperature > stopping_temperature or iteration_number > stopping_iter:
  # The consecutive-swap neighbour generator is expected to perform better than the arbitrary-swap one
  [i,j] = sorted(random.sample(range(number_of_cities),2))

  new_tour = current_tour.get_new_tour_with_swapped_cities(i,j)

  if(acceptance_probability(current_tour.tour_distance, new_tour.tour_distance, temperature) > random.uniform(0,1)):
    current_tour = copy.deepcopy(new_tour)

  if(current_tour.tour_distance < best_solution.tour_distance):
    best_solution = copy.deepcopy(current_tour)

  distance_timeseries.append(best_solution.tour_distance)
  solution_timeseries.append(best_solution.tour_list)

  temperature *= 1-cooling_rate
  iteration_number += 1



print("Final tour distance: "+str(best_solution.tour_distance))

plt.plot([t.x for t in best_solution.tour_list],[t.y for t in best_solution.tour_list],"b")
plt.plot([t.x for t in [best_solution.tour_list[-1], best_solution.tour_list[0]]],\
  [t.y for t in [best_solution.tour_list[-1], best_solution.tour_list[0]]],"b")

plt.show()

fig2 = plt.figure(2)
ax = plt.axes(figure=fig2, title="TSP distance evolution", xlim=(0, grid_size), ylim=(0, grid_size))
plt.plot(distance_timeseries,'.')
plt.show()
