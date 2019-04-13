import matplotlib
matplotlib.use('TkAgg')
import random, numpy, math, copy, matplotlib.pyplot as plt

number_of_cities = 48
grid_size = 1000
cities = [random.sample(range(grid_size), 2) for x in range(number_of_cities)]
tour = random.sample(range(number_of_cities),number_of_cities)

def acceptance_func(i,j,temperature):
  s1 = sum(([ math.sqrt(sum([(cities[tour[(k+1) % number_of_cities]][d] - cities[tour[k % number_of_cities]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]))
  s2 = sum(([math.sqrt(sum([(cities[newTour[(k+1) % number_of_cities]][d] - cities[newTour[k % number_of_cities]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]))
  return math.exp( ( s1 - s2) / temperature)

for temperature in numpy.logspace(0,5,num=100000)[::-1]:
  [i,j] = sorted(random.sample(range(number_of_cities),2))
  newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:]
  if acceptance_func(i,j,temperature) > random.random():
    tour = copy.copy(newTour)
    
plt.plot([cities[tour[i % number_of_cities]][0] for i in range(number_of_cities+1)], [cities[tour[i % number_of_cities]][1] for i in range(number_of_cities+1)], 'xb-');
plt.show()