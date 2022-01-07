customers=list(map(int,input().split()))
biscuit=list(map(int,input().split()))

for i in range(len(biscuit)):
    if biscuit[i] in customers:
        customers.remove(biscuit[i])
    else:
        print(len(customers))
        break