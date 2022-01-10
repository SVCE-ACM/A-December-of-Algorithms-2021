# #05 Biscuit Bonanza!
# @DSAghicha (Darshaan Aghicha)
def check(customers: list[int], biscuits: list[int]) -> None:
    if not customers or not biscuits or biscuits[0] not in customers:
        print(f"Customers that are unable to eat = {len(customers)}")
        return
    
    if customers[0] == biscuits[0]:
        customers.pop(0)
        biscuits.pop(0)
        # print(f"Front customer takes the top biscuit and leaves the line making customers = {customers} and biscuits = {biscuits}.")
    else:
        first_item = customers[0]
        customers.pop(0)
        customers.append(first_item)
        # print(f"Front customer leaves the top biscuit and returns to the end of the line making customers = {customers}.")
    check(customers, biscuits)


def main() -> None:
    try:
        customers: list[int] = [int(choice) for choice in input("Enter customers choice (space separated): ").split(' ')]
        biscuits: list[int] = [int(choice) for choice in input("Enter biscuits choice (space separated): ").split(' ')]
        check(customers, biscuits)
    except ValueError:
        print("One or more values were not integer!")


if __name__ == '__main__':
    # customers = [1,1,0,0,1,0]
    # biscuits = [0,1,0,1,1,1]
    # check(customers, biscuits)
    main()
