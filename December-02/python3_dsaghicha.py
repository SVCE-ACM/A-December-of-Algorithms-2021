# #02 Bingo!
# @DSAghicha (Darshaan Aghicha)

def sum_of_squares(number: int) -> None:
    """
    Calculates sum of square of digits in the number, and calls itself until condition fails.
    Conditions:
        - number is not a positive integer. (prints "NO")
        - sum = 1. (prints "YES")
    Args:
        number: int
    Returns:
        None
    """
    if number > 0:
        num: list[int] = [int(n) for n in str(number)]
        sum_num: int = 0
        for n in num:
            sum_num += n ** 2
        try:
            if sum_num != 1:
                sum_of_squares(sum_num)
            else:
                print("YES")
        except RecursionError:
            print("NO")
    else:
        print("NO")


def main() -> None:
    num: int = int(input("Enter the Number: "))
    sum_of_squares(num)


if __name__ == '__main__':
    main()
