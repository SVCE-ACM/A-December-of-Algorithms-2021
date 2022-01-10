# #12 Ford vs Ferrari!
# @DSAghicha (Darshaan Aghicha)
def superiority(arr: list[int]) -> None:
    if len(arr) <= 1:
        return arr

    cars = req_split(arr)
    for i in range(len(cars)):
        if cars[i][0] == '-':
            if cars[i][1] < cars[i - 1][1]:
                arr.pop(i)
                superiority(arr)
            elif cars[i][1] == cars[i - 1][1]:
                arr.pop(i)
                arr.pop(i - 1)
                superiority(arr)
            else:
                arr.pop(i - 1)
                superiority(arr)
        
    return arr


def req_split(arr: list[int]) -> list[str, int]:
    final_arr = []
    for num in arr:
        if num < 0:
            cell = ['-', int(str(num)[1])]
        else:
            cell = ['+', num]
        final_arr.append(cell)
    return final_arr


def main() -> None:
    try:
        cars: list[int] = [int(car) for car in input("Enter the row of cars: ").split(' ')]
        print(superiority(cars))
    except ValueError:
        print("One or more cars were not correct!\n\n")
        main()

if __name__ == "__main__":
    main()
