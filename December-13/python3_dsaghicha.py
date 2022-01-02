# #13 Desert Shopping!
# @DSAghicha (Darshaan Aghicha)
def sales(clients:int, diamonds:int, diamond_eval: list[list[int]], client_req: list[list[int]]) -> None:
    sales:int = []
    t = 0
    for j in range(clients):
        print(f"k{j} = {client_req[j][0]}, r{j} = {client_req[j][1]}")
    for p in range(diamonds):
        print(f"m{p} = {diamond_eval[p][0]}, n{p} = {diamond_eval[p][1]}")
    print()

    for client in range(clients):
        interested:int = 0
        for diamond in range(diamonds):
            purity: bool = client_req[client][0] < diamond_eval[diamond][0]
            cost: bool = client_req[client][1] >= diamond_eval[diamond][1]
            print(purity, cost)
            if purity and cost:
                interested += 1
                t += 1
        
        sales.append(interested)
    
    print(sales)
    print("T: ", t)
    print(f"Maximum number of diamonds sold = {max(sales)}")


def main() -> None:
    try:
        x: int = int(input("Enter number of unsold diamonds: "))
        diamond_eval: list[list[int]] = []
        client_req: list[list[int]] = []
        z: int = int(input("Enter number of clients: "))

        for j in range(z):
            kj: int = int(input(f"Enter client {j}'s requested purity level: "))
            rj: int = int(input(f"Enter client {j}'s price: ")) 
            client_req.append([kj, rj])

        for p in range(x):
            mp: int = int(input(f"Enter diamond {p}'s purity level: "))
            np: int = int(input(f"Enter diamond {p}'s minimum price: ")) 
            diamond_eval.append([mp, np])
        
        print(z, x, diamond_eval, client_req)
        sales(z, x, diamond_eval, client_req)
    except ValueError:
        print("I expected a number!!\n\n")
        main()


if __name__ == "__main__":
    main()
    