class Solution:
  def __init__(self, customers, biscuits):
    self.customers = customers
    self.biscuits = biscuits

  def solve(self):
    # No of biscuits in stack.
    stack_len = len(self.biscuits)
    cnt = 0
    
    # Complete one round of iteration and if the buiscuits stack 
    # is changed or not.
    while cnt <  len(self.customers):
      # When customers likes the buiscuit.
      if self.customers[0] == self.biscuits[0]:
        self.customers = self.customers[1:]
        self.biscuits = self.biscuits[1:]
      else:
        # Customer removed and placed at end of Queue.
        curr_customer = self.customers[0]
        self.customers = self.customers[1:]
        self.customers.append(curr_customer)
        cnt += 1

    # Stack length not changed indicates that no 
    # customer in the queue prefers the buiscuit at
    # the top of the stack.
    if len(self.biscuits) == stack_len:
      print(f"Customers that are unable to eat = {len(self.customers)}")
    else:
      # Keep solving until no user prefers the buiscuit at top
      # of the stack or until all biscuits are over.
      self.solve()


def get_list_from_string(string):
  string = string[1:len(string)-1]
  string = string.replace(' ', '').split(',')
  new_list = [int(ele) for ele in string]
  return new_list


def main():
  customers = input("customers = ")
  customers = get_list_from_string(customers)
  biscuits = input("biscuits = ")
  biscuits = get_list_from_string(biscuits)
  obj = Solution(customers=customers, biscuits=biscuits)
  obj.solve()


if __name__ == "__main__":
  main()