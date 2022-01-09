# Catch Me If You Can!
# @DSAghicha (Darshaan Aghicha)
def leos_fate(X: int, A: int, a: list[int]):
    odd_pos = even_pos = 0
    for pos in a:
        if pos % 2 == 0:
            even_pos += 1
        else:
            odd_pos += 1
    
    if odd_pos == 0 or even_pos == 0:
        return (X, 1)
    else:
        return (odd_pos, -1) if odd_pos > even_pos else (even_pos, -1)


def main() -> None:
    try:
        no_ranger: int = int(input("Enter number of rangers (X): "))
        leo_pos: int = int(input("Enter position of Leo (A): "))
        ranger_pos: list[int] = [int(x) for x in input("Enter position of ranger(s): ").split(" ")]

        fallen_ranger, fate = leos_fate(no_ranger, leo_pos, ranger_pos)

        fate_str: str = "and he escapes" if fate == 1 else "but gets caught"
        print(f"Leo can eliminate {fallen_ranger} ranger(s) {fate_str}.")
        print(f"{fallen_ranger} {fate}")
        
    except ValueError:
        print("Invalid Input!")

if __name__ == "__main__":
    main()
