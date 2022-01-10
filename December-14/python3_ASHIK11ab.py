import ast

class Solution:
  def __init__(self, chapters):
    self.chapters = chapters

  def solve(self, deadline):
    concepts_to_study = 1
    while True:
      req_hours = 0
      for concepts in self.chapters:
        req_time = find_req_time_to_study(concepts, concepts_to_study)
        req_hours += req_time
      if req_hours <= deadline:
        print(concepts_to_study)
        break
      # Increase the value of `y` if the current value does not fit it.
      concepts_to_study += 1


def find_req_time_to_study(concepts, concepts_to_study):
  hours_cnt = 0
  while concepts > 0:
    concepts = concepts - concepts_to_study
    hours_cnt += 1
  return hours_cnt


def main():
  chapters = ast.literal_eval(input("chapter = "))
  deadline = int(input("x = "))
  s = Solution(chapters=chapters)
  s.solve(deadline)

  
if __name__ == "__main__":
  main()