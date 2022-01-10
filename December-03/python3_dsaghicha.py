# #03 Lotto!
# @DSAghicha (Darshaan Aghicha)
def search_grid(board: list[list[str]], name: str) -> bool:
    ROW, COL = len(board), len(board[0])
    path = set()

    def search(row, col, i):
        if i == len(name):
            return True
        
        if (row < 0 or col < 0 or row >= ROW or col >= COL or name[i] != board[row][col] or (row, col) in path):
            False
        
        path.add((row, col))
        
        result = (search(row + 1, col, i + 1) or search(row - 1, col, i + 1) or search(row, col + 1, i + 1) or search(row, col - 1, i + 1))

        return result
    
    for row in range(ROW):
        for col in range(COL):
            if search(row, col, 0):
                return True
    
    return False


def main():
    try:
        R: int = int(input("Enter the number of rows: "))
        C: int = int(input("Enter the number of columns: "))
        matrix: list[list[str]] = []

        for _i in range(C):
            letters: list[str] = input(f"Enter {R} letters (space seperated): ").split(' ')

            while len(letters)  != R:
                print("\nIt seems like you missed some letters!\n")
                letters: list[str] = input(f"Re-enter {R} letters (space seperated): ").split(' ')
            matrix.append([letter.upper() for letter in letters])
        
        word: str = input("Enter word to be searched: ")
        while len(word) < 2:
            print("Please input a proper word!")
            word: str = input("Re-enter word to be searched: ")
        
        print(search_grid(matrix, word.upper()))
    except ValueError:
        print("It was not a number!\n\n")
        main()


if __name__ == "__main__":
    # grid: list[list[str]] = [["D","J","O","G"],["W","B","H","S"],["T","Z","N","E"]]
    # print(search_grid(grid, name="JOHN"))
    main()
