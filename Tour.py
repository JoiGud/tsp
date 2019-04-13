import math
import random
from city import City
import copy
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
      return self.city_list

    def init_tour_list(self):
      self.tour_list = random.sample(self.city_list, self.number_of_cities)
      # self.tour_list.append(self.tour_list[0]) # Make it a roundtrip

    def get_total_distance(self):
      distance = 0
      for i, o in enumerate(self.tour_list[:-1]):
        distance += o.distance(self.tour_list[i+1])
      distance += self.tour_list[-1].distance(self.tour_list[0]) # Make it a roundtrip
      return distance

    def get_new_tour_with_swapped_cities(self, i, j):
      tmp_tour = copy.deepcopy(self)
      tmp_tour.tour_list[i:j] = reversed(tmp_tour.tour_list[i:j])
      # tmp_tour.tour_list[i:j] = self.tour_list[j]
      # tmp_tour.tour_list[j] = self.tour_list[i]
      return tmp_tour
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"