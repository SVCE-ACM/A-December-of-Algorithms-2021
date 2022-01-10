class Solution:
  def __init__(self, templars):
    self.templars = [templar for templar in templars]

  def solve(self):
    left = 0
    right = len(self.templars) - 1
    swap_cnt = 0
    # Always maintain `templar U` in left and `templar T` in right.
    # If above does not hold then swap and increment swap count by 1.
    while left != right:
      if self.templars[left] == 'T':
        if self.templars[right] == 'U':
            (self.templars[left], self.templars[right]) = (self.templars[right], self.templars[left])
            swap_cnt += 1
        else:
          right -= 1
      else:
        left += 1
    print(swap_cnt)

def main():
  templars = input()
  s = Solution(templars)
  s.solve()

if __name__ == "__main__":
  main()