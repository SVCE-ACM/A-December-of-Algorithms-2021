# #10 Juicy Orange Field!
# @DSAghicha (Darshaan Aghicha)
class Solution:
    def __init__(self, size: int, field: list[list[int]]) -> None:
        # * Starting Position (0, 0)
        self.x, self.y = 0, 0
        # * Destination Position
        self.X, self.Y = size - 1, size - 1
        self.field = field
        self.oranges = 0
    
    def move_in(self) -> None:
        if self.y != self.Y:
            right_cell: int =  self.field[self.x][self.y + 1]

            if right_cell == 1:
                self.oranges += 1
                self.field[self.x][self.y + 1] = 0
            if right_cell == 1 or right_cell == 0:
                self.y += 1
                return
        if self.x != self.X:
            down_cell: int = self.field[self.x + 1][self.y]
            
            if down_cell == 1:
                self.oranges += 1
                self.field[self.x + 1][self.y] = 0
            if down_cell == 1 or down_cell == 0:
                self.x += 1
                return
    
    def move_out(self) -> None:
        if self.Y != 0:
            right_cell: int =  self.field[self.X][self.Y - 1]

            if right_cell == 1:
                self.oranges += 1
                self.field[self.X][self.Y - 1] = 0
            if right_cell == 1 or right_cell == 0:
                self.Y -= 1
                return
        if self.X != 0:
            down_cell: int = self.field[self.X - 1][self.Y]
            
            if down_cell == 1:
                self.oranges += 1
                self.field[self.X - 1][self.Y] = 0
            if down_cell == 1 or down_cell == 0:
                self.X -= 1
                return
    
    def start(self) -> int:
        while (self.x, self.y) != (self.X, self.Y):
            self.move_in()
        while ((self.X, self.Y)) != (0, 0):
            self.move_out()
        return self.oranges



def main() -> None:
    try:
        n = int(input("Enter maze size: "))
        field: list[list[int]] = []
        for _i in range(n):
            row: list[int] = [int(cell) for cell in input(f"Enter {n} cells (space seperated): ").split(' ')]
            for cell in row:
                if cell not in [0, 1, -1]:
                    print(cell)
                    print("Invalid Input!")
                    main()

            field.append(row)
        print(Solution(n, field).start())
    except ValueError:
        print("It was not a number!\n\n")
        main()

if __name__ == "__main__":
    main()
