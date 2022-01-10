import ast

class Solution:
  def __init__(self, no_understudies, req_understudies, abilities):
    self.no_understudies = no_understudies
    self.req_understudies = req_understudies
    self.abilities = abilities

  def solve(self):
    candidate_teams = combinations(self.abilities, self.req_understudies)
    base_periods = []
    for team in candidate_teams:
      base_period = 0
      for member in team:
        base_period += max(team) - member
      base_periods.append(base_period)
    print(f"Base number of periods required = {min(base_periods)}")
    return


def combinations(array, k, candidates=[], result=[]):
  # When k is 0 (when one of the k item combination is generated) then
  # add it to the result.
  if k == 0:
    result.append(candidates[:])
    return
  # Pick an element from the list and find the remaining combinations.
  # After finding the result remove the picked element and proceed
  # with the next elements.
  for i in range(0, len(array)):
    candidates.append(array[i])
    combinations(array[i+1:], k-1, candidates, result)
    candidates.pop()
  return result


def main():
  no_understudies = int(input("N = "))
  req_understudies = int(input("P = "))
  understudies_ability = ast.literal_eval(input("N = "))
  s = Solution(no_understudies, req_understudies, understudies_ability)
  s.solve()

if __name__ == "__main__":
  main()