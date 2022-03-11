from maths import distance_between
from utils import i_am_closest
def closest(origin, li, heads):
  closest_distance = 9999999999
  #thisIndex = 0
  for dct in li:
    if distance_between(origin, dct) < closest_distance:
      closest_distance = distance_between(origin, dct)
      #thisIndex = li.index(dct)
  return closest_distance
