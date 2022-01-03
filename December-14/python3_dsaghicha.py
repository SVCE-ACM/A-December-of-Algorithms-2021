# #14 The Math Test!
# @DSAghicha (Darshaan Aghicha)
def no_concepts(chapters: list[int], hours) -> int:
    total = sum(chapters)
    concepts = total // hours if total % hours == 0 else (total // hours) + 1
    hour = 0

    while True:
        for chapter in chapters:
            hour += chapter // concepts if chapter % concepts == 0 else (chapter // concepts) + 1
        
        if hour == hours:
            return concepts 
    
        concepts += 1
        hour = 0



    

def main() -> None:
    try:
        n: list[int] = [int(N) for N in input("Enter chapters: (space separated) ").split(" ")]
        x: int = int(input("Enter number of hours to prepare for the exam: "))

        concepts = no_concepts(n, x)
        print(f"She can study {concepts} concepts from her chapters per hour such that, she can cover all the concepts from the chapters within {x} hours.")
    except ValueError:
        print("Not a Number!!")
        main()


if __name__ == "__main__":
    main()
