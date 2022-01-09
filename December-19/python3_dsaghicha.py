"""
@title: Winter is coming
@author: DSAghicha (Darshaan Aghicha)
@access: public
"""
def mandatory_courses(course: list[list[int]],answer: list[list[int]]) -> tuple[list[bool], int]:
    result: list[bool] = []
    indirect_dependency: list[int] = []
    indirect_index: int = -1
    for i in range(len(course)):
        if i + 1 < len(course) and course[i][1] == course[i+1][0]:
            pr: list[int] = [course[i][0], course[i+1][1]]
            indirect_dependency = pr if pr not in course else []

    for answers in answer:
        if indirect_dependency == answers:
            indirect_index = answer.index(answers)
            result.append(True)
        else:
            result.append(answers in course)
    return (result, indirect_index)


def main() -> None:
    try:
        num: int = int(input("Enter number of courses: "))
        courses: list[list[int]] = []
        for _ in range(num - 1):
            print("Enter course: ", end='')
            course = [int(x) for x in input().split(" ")]
            if len(course) != 2:
                raise ValueError
            courses.append(course)
        
        answers: list[list[int]] = []
        for _ in range(2):
            print("Enter answer: ", end='')
            answer = [int(x) for x in input().split(" ")]
            if len(answer) != 2:
                raise ValueError
            answers.append(answer)
        output, format_index = mandatory_courses(courses, answers)
        print(f"Output: {output}")
        print(f"\n{'-' * 10}\n")
        for i in range(len(answers)):
            if format_index == i:
                print(format_index)
                print(f"Course {answers[i][0]} is mandatory to take up course {answers[i][1]}.")

            elif output[i] is True:
                print(f"Course {answers[i][0]} is mandatory to take up course {answers[i][1]}.")
            elif output[i] is False:
                print(f"Course {answers[i][0]} is not mandatory to take up course {answers[i][1]}.")
    
    except ValueError:
        print("\nInvalid Input!\n")
        main()


if __name__ == "__main__":
    main()
