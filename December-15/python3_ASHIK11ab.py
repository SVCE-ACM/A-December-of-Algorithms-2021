import ast

class Solution:
  def __init__(self, orders, deadline):
    self.orders = orders
    self.deadline = deadline


  def solve(self):
    # `y` -> no of bracelets to be made in a day to deliver all orders
    # on time. The starting value of `y` will be >= maximum element in 
    # the orders list since, no order can be half complete on the end 
    # of a day.
    y = max(self.orders)

    while True:
      cont_sub_arrays = find_cont_sub_arrays(self.orders[:], y)
      if len(cont_sub_arrays) <= self.deadline:
        print(y)
        break
      else:
        y += 1


def find_cont_sub_arrays(array, y):
  """ Returns the continuous sub arrays where each sub array sum is <= y. """
  cont_sub_arrays = []
  outer_index = 0

  while array != [] :
    temp = []
    for j in range(len(array)):
      cont_sub_array = array[:j+1]
      # Store the continuous sub arrays temporarily since we 
      # are only intrested in the longest continuous sub array
      # whose sum is <= y.
      if sum(cont_sub_array) <= y:
        temp = cont_sub_array
        # If a valid sub array found is the last sub array of the array
        # then add it to the list of sub arrays.
        if j+1 == len(array):
          cont_sub_arrays.append(temp)
          array = array[j+1:]
      else:
        cont_sub_arrays.append(temp)
        array = array[j:]
        break
  return cont_sub_arrays


def main():
  orders = ast.literal_eval(input("number of bracelets = "))
  no_of_days = int(input("n = "))
  s = Solution(orders=orders, deadline=no_of_days)
  s.solve()


if __name__ == "__main__":
  main()