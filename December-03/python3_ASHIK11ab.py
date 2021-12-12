class Solution:
  def __init__(self, board, req_name):
    self.board = board
    self.req_name = req_name
    self.visited_cells = []
    self.solution_reached = False

  # Use cells in board.
  def cell_in_board(self, cell):
    return cell[0] >= 0 and cell[0] < len(self.board) and \
      cell[1] >= 0 and cell[1] < len(self.board[0])


  # Find next required alphabet.
  def find_next_character(self, scanning_index, curr_cell):
    if scanning_index == len(self.req_name):
      self.solution_reached = True
      return

    left_cell = (curr_cell[0], curr_cell[1]-1)
    top_cell = (curr_cell[0]-1, curr_cell[1])
    right_cell = (curr_cell[0], curr_cell[1]+1)
    bottom_cell = (curr_cell[0]+1, curr_cell[1])

    candidate_cells = [left_cell, top_cell, right_cell, bottom_cell]

    # For a given alphabet the neighbouring cells are left, top
    # right, bottom.
    for cell in candidate_cells:
      if self.cell_in_board(cell) and cell not in self.visited_cells \
        and self.board[cell[0]][cell[1]] == self.req_name[scanning_index]:
        scanning_index += 1
        self.visited_cells.append(cell)
        self.find_next_character(scanning_index, cell)

        if not self.solution_reached:
          # Undo current step if solution is not possible.
          scanning_index -= 1
          self.visited_cells.pop()
        else:
          return


  def solve(self):
    # Scanning index -> index of the alphabet of name to be 
    # searched in the board.
    scanning_index = 0
    # Look for the initial alphabet in the board.
    for row in range(len(self.board)):
      # Since the dimensions of all rows are same.
      for col in range(len(self.board[0])):
        if self.board[row][col] == self.req_name[scanning_index]:
          scanning_index += 1
          curr_cell = (row, col)
          self.visited_cells.append(curr_cell)
          self.find_next_character(scanning_index, curr_cell)

          if not self.solution_reached:
            # Undo current step if solution is not possible.
            scanning_index -= 1
            self.visited_cells.pop()
          else:
            break

    if self.solution_reached:
      print("YES")
    else:
      print("NO")


def main(board, name):
  obj = Solution(board, name)
  obj.solve()


if __name__ == "__main__":
  main(board=[["D","J","O","G"],["W","B","H","S"],["T","Z","N","E"]], name="JOHN")