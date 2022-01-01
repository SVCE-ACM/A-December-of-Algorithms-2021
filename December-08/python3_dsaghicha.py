# #08 Anomalous Counter!
# @DSAghicha (Darshaan Aghicha)
def counter_value(timer: int) -> int:
    if timer == 0:
        return 0
    
    counter_dial: int = 0
    prev_dial: int = 0
    cycle_dial: int = 0
    counter = 0
    while timer > counter_dial:
        counter += 1
        prev_dial = counter_dial
        counter_dial = counter_dial + 3 * (2 ** cycle_dial)
        cycle_dial += 1
    
    return 3 * (2 ** (cycle_dial - 1)) - (timer - prev_dial) + 1



def main() -> None:
    try:
        time: int = int(input("Enter time: "))
        value: int = counter_value(time)
        print(f"Counter value = {value}")
    except ValueError:
        print("I expected a number!!\n\n")
        main()

if __name__ == "__main__":
    main()
