# Twinkling Bracelets!
# @DSAghicha (Darshaan Aghicha)
def bracelets_per_day(no_bracelets: list[int], days: int) -> int:
    max_value: int = max(-1, max(no_bracelets))
    for i in range(max_value, sum(no_bracelets)):
        bracelets: int = sum(no_bracelets) // i
        if sum(no_bracelets) % i != 0:
            bracelets += 1   
        if bracelets <= days:
            return i


def main() -> None:
    try:
        bracelets: int = [int(bracelet) for bracelet in input("Enter number of bracelets (space separated): ").split(" ")]
        no_days:int = int(input("Enter maximum number of n days for the bracelets to be delivered to the customers: "))
        print(f'\nPinky can make {bracelets_per_day(bracelets, no_days)} bracelets and deliver them in a day such that she delivers all the orders within {no_days} days.\n')
    except ValueError:
        print("Improper input!!")
        main()


if __name__ == "__main__":
    main()