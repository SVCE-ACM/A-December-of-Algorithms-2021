import ast

class Solution:
  def __init__(self, grid):
    self.grid = grid
    self.max_oranges = 0


  def go_to_first_cell(self, row, col, oranges):

    if (row, col) == (0, 0):
      self.max_oranges = max(oranges, self.max_oranges)
      return

    cell_value = self.grid[row][col]

    if self.grid[row][col] == 1:
      oranges += 1
      self.grid[row][col] = 0

    # Make top move.
    if can_make_move(self.grid, row-1, col):
      self.go_to_first_cell(row-1, col, oranges)


    # Make left move.
    if can_make_move(self.grid, row, col-1):
      self.go_to_first_cell(row, col-1, oranges)
    
    self.grid[row][col] = cell_value


  def solve(self, row, col, oranges):

    row_len = len(self.grid)
    col_len = len(self.grid[0])
    cell_value = self.grid[row][col]

    if self.grid[row][col] == 1:
      oranges += 1
      self.grid[row][col] = 0

    # Go to first cell if last cell is reached.
    if (row, col) == (row_len-1, col_len-1):
      self.go_to_first_cell(row, col, oranges)
      return

    # Make right move.
    if can_make_move(self.grid, row, col+1):
      self.solve(row, col+1, oranges)

    # Make down move.
    if can_make_move(self.grid, row+1, col):
      self.solve(row+1, col, oranges)
    # After both right and down paths are taken restore the value
    # of the cell so that it will be used by its previous paths.
    self.grid[row][col] = cell_value


def can_make_move(grid, row, col):
  return (row >= 0 and row < len(grid)) and (col >= 0 and col < len(grid[0])) \
    and grid[row][col] != -1


def main():
  grid = ast.literal_eval(input("field = "))
  s = Solution(grid=grid)
  s.solve(0, 0, oranges=0)
  print(s.max_oranges)

if __name__ == "__main__":
  main()