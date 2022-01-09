class Solution:
  def __init__(self):
    self.diamonds_sold = 0

  def solve(self, clients, diamonds, diamonds_sold_cnt=0):
    # Store the count of previously sold diamonds if their value is 
    # greater than the aldready sold diamonds count.
    self.diamonds_sold = max(self.diamonds_sold, diamonds_sold_cnt)

    # No further solution is possible when there are no clients to buy
    # diamonds are when there are no diamonds to buy.
    if len(clients) == 0 or len(diamonds) == 0:
      return

    for (client_index, client) in enumerate(clients):
      # Find diamonds which satisfy the clients requirement.
      qualified_diamonds = find_qualified_diamonds(client, diamonds)

      remaining_clients = clients[:client_index] + clients[client_index+1:]

      # Continue with next client if there are no diamonds which satisfy
      # the clients requirements.
      if len(qualified_diamonds) == 0:
        continue
      
      # Compute the solution by allowing client to choose all diamonds
      # one by one and finding the best diamond which can be sold to 
      # the client to sell maximum number of diamonds among all clients.
      for diamond_index in range(len(qualified_diamonds)):
        # Remove the diamond chosen by client and compute the solution
        # using the remaining diamonds.
        remaining_diamonds = qualified_diamonds[:diamond_index] + qualified_diamonds[diamond_index+1:]
        
        self.solve(remaining_clients, remaining_diamonds, diamonds_sold_cnt+1)


def find_qualified_diamonds(client_req, diamonds):
  qualified_diamonds = []
  for diamond in diamonds:
    # A diamond is qualified if its purity level is greater than client
    # requirement purity level and if the diamond price is lesser than or equal
    # to the client's requirement price.
    if diamond[0] > client_req[0] and diamond[1] <= client_req[1]:
      qualified_diamonds.append(diamond)
  return qualified_diamonds


def main():
  z = int(input("z = "))
  x = int(input("x = "))
  clients_req = []
  diamonds = []

  print()
  for i in range(z):
    client_purity_req = int(input(f"k{i} = "))
    client_budget = int(input(f"r{i} = "))
    client_req = (client_purity_req, client_budget)
    clients_req.append(client_req)
  
  print()
  for i in range(x):
    diamond_purity = int(input(f"m{i} = "))
    diamond_price = int(input(f"n{i} = "))
    diamond_spec = (diamond_purity, diamond_price)
    diamonds.append(diamond_spec)

  s = Solution()
  s.solve(clients_req, diamonds)
  print(f"\nMaximum number of diamonds sold = {s.diamonds_sold}")


if __name__ == "__main__":
  main()