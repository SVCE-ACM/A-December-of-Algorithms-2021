class Solution:
  def __init__(self, time):
    self.time = time

  def solve(self):
    if self.time == 0:
      print("counter value: 0")
      return
    # Counter initial value is 3 but is set as 4 to keep the counter
    # value at 3 during the first iteration.
    counter_val = 4
    prev_counter_val = 3
    for index in range(0, self.time):
      # when counter value is 1 reset it with twice the value
      # of the previous round counter's initial value.
      if counter_val == 1:
        temp = counter_val
        counter_val = 2*prev_counter_val
        prev_counter_val = counter_val
      else:
        counter_val -= 1

    print(f"counter value: {counter_val}")

def main():
  time = int(input("time: "))
  s = Solution(time=time)
  s.solve()

if __name__ == "__main__":
  main()