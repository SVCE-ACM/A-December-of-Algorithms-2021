"""
@title: Transform to Checkerboard
@author: DSAghicha (Darshaan Aghicha)
@access: public
"""
from collections import Counter


def moves_to_checkerboard(initial_board: list[list[int]]) -> int:
    n: int = len(initial_board) # Size of the Board
    inverted_board: list[list[int]] = [[row[i] for row in initial_board] for i in range(n)]
    row_count = list(Counter([tuple(row) for row in initial_board]).items())
    col_count = list(Counter([tuple(row) for row in inverted_board]).items())

    if len(row_count) != 2 or len(col_count) != 2:
        return -1 # Task is impossible!!!
    
    h_pattern = list([1, 0] * ((n // 2) + 1))[:n]
    l_pattern = list([0, 1] * ((n // 2) + 1))[:n]
    
    # Number of ROWS needed to be flipped
    nr1: int = sum([1 for i in range(n) if row_count[0][0][i] != h_pattern[i]])
    nr2: int = sum([1 for i in range(n) if row_count[0][0][i] != l_pattern[i]])

    # Number of COLUMNS needed to be flipped
    nc1: int = sum([1 for i in range(n) if col_count[0][0][i] != h_pattern[i]])
    nc2: int = sum([1 for i in range(n) if col_count[0][0][i] != l_pattern[i]])

    # Checking if required number of Rows & Columns is EVEN
    nr = [x for x in (nr1, nr2) if x % 2 == 0]
    nc = [x for x in (nc1, nc2) if x % 2 == 0]

    return int(min(nr) // 2 + min(nc) // 2)



def main() -> None:
    try:
        board: list[list[int]] = []
        n: int = int(input("Enter size of your board: "))
        print(f"Enter a {n} x {n} board:\n(Hit Enter for next column and each number should be space separated)")
        for col in range(n):
            row = [int(num) for num in input().split()]

            other_number = False
            for elem in row:
                if elem not in [1, 0]: other_number = True
            if len(row) != n or other_number: raise ValueError
            
            board.append(row)
        
        print(moves_to_checkerboard(board))
    except ValueError:
        print("Invalid Input!")
        main()


if __name__ == "__main__":
    main()
