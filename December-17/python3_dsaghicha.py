"""
@title: The Bossy Manager
@author: DSAghicha (Darshaan Aghicha)
@access: public
"""
def min_time(task_size, processing_time, no_tasks) -> int:
    min_time: int = 0
    time: int = 0 # Time for each single task
    size: int = len(task_size)
    for i in range(size):
        time = no_tasks[i] // task_size[i]
        if no_tasks[i] % task_size[i] != 0: time += 1
        min_time = max(min_time, (time * processing_time[i]))
    
    return min_time


def main() -> None:
    try:
        task_size: list[int] = [int(x) for x in input("Enter task size (space separated): ").split(" ")]
        processing_time: list[int] = [int(x) for x in input("Enter processing time (space separated): ").split(" ")]
        no_tasks: list[int] = [int(x) for x in input("Enter number of tasks (space separated): ").split(" ")]
        if len(task_size) != len(processing_time) != no_tasks:
            raise Exception
        
        req_time: int = min_time(task_size, processing_time, no_tasks)
        print(f"The minimun time to process all the tasks is {req_time}.")
    except ValueError:
        print("Invalid Input")
        main()
    
    except Exception:
        print("\nIt seems like you skipped one or more values.\nLet's try again!\n")
        main()


if __name__ == "__main__":
    main()
