"""
@title: Connections
@author: DSAghicha (Darshaan Aghicha)
@access: public
"""
def connections(matrix: list[list[int]]) -> int:
    n: int = len(matrix) # Size of Matrix
    least_connections: int = 0
    x, y = None, None

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                if x is None:
                    x, y = i, j
                else:
                    least_connections += abs(x - i) + abs(y - j)
    
    return least_connections - 1

def main() -> None:
    try:
        grid: list[list[int]] = []
        size: int = int(input("Enter Grid Size: "))
        print("Enter Matrix: (space separated for row, Enter for new column)")
        for num in range(size):
            col: list[int] = [int(x) for x in input().split(" ")]
            if len(col) != size:
                raise ValueError
            grid.append(col)
        print(f"You must flip at least {connections(grid)} 0(s) to connect the two houses.")
    
    except ValueError:
        print("\nInvalid input!\n")
        main()

if __name__ == "__main__":
    main()
