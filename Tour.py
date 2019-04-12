import math
import random
from City import City
import pdb

class Tour:
    def __init__(self, number_of_cities, grid_size):
      self.number_of_cities = number_of_cities
      self.grid_size = grid_size
      self.city_list = []
      self.tour_list = []

    def init_city_list(self):
      for dummy in range(self.number_of_cities):
        [x,y] = random.sample(range(self.grid_size), 2)
        self.city_list.append(City(x,y))
        # plt.plot(x,y,"or")
      return self.city_list

    def init_tour(self):
      self.tour_list = random.sample(self.city_list, self.number_of_cities)
      self.tour_list.append(self.tour_list[0]) # Make it a roundtrip

    def get_total_distance(self):
      distance = 0
      # pdb.set_trace()
      for i, o in enumerate(self.city_list[:-1]):
        distance += o.distance(self.city_list[i+1])
      return distance
    
    # def distance(self, city):
    #     xDis = abs(self.x - city.x)
    #     yDis = abs(self.y - city.y)
    #     distance = math.sqrt((xDis ** 2) + (yDis ** 2))
    #     return distance
    
    # def __repr__(self):
    #     return "(" + str(self.x) + "," + str(self.y) + ")"