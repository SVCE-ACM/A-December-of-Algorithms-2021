class Solution:
  def __init__(self, buildings, planes):
    self.buildings = buildings
    self.planes = planes

  def solve(self):
    # For each plane find the number of buildings which can recieve
    # food from the plane.
    for plane_index in range(len(self.planes)):
      buildings_recieved_food_cnt = 0
      for index in range(len(self.buildings)):
        if food_delivery_possible(self.buildings[index], self.planes[plane_index]):
          buildings_recieved_food_cnt += 1
      print(buildings_recieved_food_cnt)
        

def food_delivery_possible(building, plane):
  direction = plane[0]
  point = plane[1]
  # Get three poinst of a building.
  p1 = building[0]
  p2 = building[1]
  p3 = building[2]

  # Food on a plane can be delivered to a building if the plane
  # flies over the building.
  # For a given direction, if plane passes through any one of the
  # three sides of the building then the food can be delivered. 

  # dir_index -> if plane passes through 'x' take the x coordinate
  # of all points of the building or take 'y' coordinate.
  # pt (x,y) -> 0 accesses x coordinate, 1 accesses y coordinate

  dir_index = 0 if direction == 'x' else 1

  if point > min(p1[dir_index], p2[dir_index]) and point < max(p1[dir_index], p2[dir_index]):
    delivery_possible = True
  elif point > min(p1[dir_index], p3[dir_index]) and point < max(p1[dir_index], p3[dir_index]):
    delivery_possible = True
  elif point > min(p2[dir_index], p3[dir_index]) and point < max(p2[dir_index], p3[dir_index]):
    delivery_possible = True
  else:
    delivery_possible = False
  return delivery_possible


def get_coords(line):
  """ Parses a line of 6 integers and returns list of three coordinates. """
  building_coords = []
  # Extracting the coordinate points from the line input.
  coords_list = [int(pt) for pt in line if pt != ' ']
  for index in range(0, len(coords_list), 2):
    coord_x = coords_list[index]
    coord_y = coords_list[index+1]
    coords = (coord_x, coord_y)
    building_coords.append(coords)
  return building_coords


def main():
  buildings_cnt = int(input("Number of Buildings: "))
  buildings = []
  print("Coordinates of the buildings:")
  for index in range(buildings_cnt):
    line = input()
    # Parses the line and finds the three pairs of points
    # of a building.
    coords = get_coords(line)
    buildings.append(coords)
  planes_cnt = int(input("Number of jet-planes: "))
  planes = []
  for index in range(planes_cnt):
    line = input()
    # jet_info -> list having the jet direction ('x' or 'y') and 
    # the point on which the jet is moving.
    jet_info = line.split(' ')
    jet_info.remove('=')
    jet_info[1] = int(jet_info[1])
    planes.append(jet_info)
  s = Solution(buildings, planes)
  print("\nBuildings that received food:")
  s.solve()

if __name__ == "__main__":
  main()