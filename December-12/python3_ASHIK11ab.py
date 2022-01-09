import ast

class Stack:
  def __init__(self, contents=[]):
    self.array = contents

  @property
  def top(self):
    if self.length == 0:
      return None
    return self.array[0]

  @property
  def length(self):
    return len(self.array)
  
  def push(self, element):
    self.array.insert(0, element)
  
  def pop(self):
    element = self.array.pop(0)
    return element


class Solution:
  def __init__(self, cars):
    self.cars = cars


  def solve(self):
    stack1 = Stack(contents=self.cars)
    stack2 = Stack()

    while stack1.length > 0:
      if stack2.length == 0 or both_cars_in_same_direction(stack1, stack2):
        # Pop from stack 1 and push to stack 2
        ele = stack1.pop()
        stack2.push(ele)

      # Top most car in stack 1 is compared with topmost car in stack2.
      # Second car is broken if it's power is less than that of first car.
      elif abs(stack1.top) > abs(stack2.top):
        stack2.pop()
      # First car is broken if it's power is less than that of second car.
      elif abs(stack1.top) < abs(stack2.top):
        stack1.pop()
      # Both the cars are broken if their powers are equal.
      else:
        stack1.pop()
        stack2.pop()

    stack2.array.reverse()
    print(stack2.array)


def both_cars_in_same_direction(stack1, stack2):
    return (stack1.top < 0 and stack2.top < 0) \
      or (stack1.top > 0 and stack2.top > 0)


def main():
  cars = ast.literal_eval(input("cars = "))
  s = Solution(cars=cars)
  s.solve()

if __name__ == "__main__":
  main()