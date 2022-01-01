# #07 Amy helps Pawnee!
# @DSAghicha (Darshaan Aghicha)
def no_building(building_co: list[list[int]],axis: str, axis_no: int) -> list[int]:
    axis_rep: int = 0 if (axis == 'x') else 1
    success: int = 0

    for i in range(len(building_co)):
        lt: bool = False
        gt: bool = False
        for j in range(axis_rep, 6, 2):
            if building_co[i][j] < axis_no:
                lt = True
            elif building_co[i][j] > axis_no:
                gt = True
            
        if lt and gt: success += 1
    
    return success

def main() -> None:
    try:
        successful_buildings: list[int] = []

        # ? Getting Building Info
        n: int = int(input("Enter number of buildings: "))
        coordinates: list[list[int]] = []
        print("Enter coordinates of the buildings:\n(Press Enter to enter coordinates of next building)")
        for _ in range(n):
            c: list[int] = [int(i) for i in input().split(' ')]
            if len(c) == 6:
                coordinates.append(c)
            else:
                print("You entered invalid number of coordinates!")
                print("Each building must contain six coordinates\na1 b1 a2 b2 a3 b3\n\n")
                main()

        # ? Getting Plane Info
        jet_planes = int(input("Enter number of jet-planes: "))
        print("Enter axis and its coordinate (space separated):\n(Press Enter to enter coordinates of next plane)")
        for _ in range(jet_planes):
            c: list[str, int] = input().split()
            if c[0] in ['x', 'y']:
                units: int = no_building(coordinates, c[0], int(c[1]))
                successful_buildings.append(units)
            else: 
                print("Axis need to be X or Y!\n\n")
                main()
        
        # ? Printing Values
        print("Buildings that received food:", *successful_buildings, sep= " ")
    except ValueError:
        print("I expected a number!!\n\n")
        main()


if __name__ == "__main__":
    main()
    # no_building([[1, 0, 0, 2, 2, 2], [1, 3, 3, 5, 4, 0], [5, 4, 4, 5, 4, 4]], 'x', 2)
