# #06 Save The Templars!
# @DSAghicha (Darshaan Aghicha)
def swaps(data: list[str]) -> int:
    total: int = data.count('T')
    curTemplars: int = 0

    for i in range(total):
        if data[i] == 'T':
            curTemplars += 1
    
    ans = curTemplars

    for i in range(total, len(data)):
        if data[i] == 'T':
            curTemplars += 1
        
        if data[i - total] == 'T':
            curTemplars -= 1 
        
        ans = min(ans, curTemplars)
    
    return ans

def main() -> None:
    arrangement: list[str] = list(input("Enter arrangement sequence: "))
    if arrangement:
        arrangement = [i.upper() for i in arrangement]
        print(swaps(arrangement))
    else:
        print("You didn't provide the sequence!!\n\nLet's try again")
        main()



if __name__ == '__main__':
    main()
