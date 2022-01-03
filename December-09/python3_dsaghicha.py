# #09 Dream 11!
# @DSAghicha (Darshaan Aghicha)
def base_number(p:int, aptitude_ratings: list[int]) -> int:
    revised_ratings: list[int] = [aptitude_ratings[i] for i in range(p)]
    num1: int = revised_ratings[len(revised_ratings) - 1]
    ans: int = 0
    for i in range(len(revised_ratings) - 2, -1, -1):
        ans += (num1 - revised_ratings[i])
    
    return ans


def main() -> None:
    try:
        n: int = int(input("Enter number of understudies (n): "))
        p: int = int(input("Enter number of understudies you wish to pick (p): "))
        if n < 0 or p > n:
            raise Exception
        ar: list[int] = [int(N) for N in input(f"Enter the aptitude rating of {n} understudies (space separated): ").split(' ')]
        sorted(ar)

        print(f"Base number of periods required = {base_number(p, ar)}")
    
    except ValueError:
        print("I expected a number!!\n\n")
        main()
    except Exception:
        print("Invalid Inputs!!\n\n")
        main()


if __name__ == "__main__":
    main()
