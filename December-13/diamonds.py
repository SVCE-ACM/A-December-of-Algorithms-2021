x=int(input())
z=int(input())
diamonds=[]
clients=[]
for j in range(z):
    clients.append(list(map(int,input().split())))

for i in range(x):
    diamonds.append(list(map(int,input().split())))

sale=0
clients.sort()
diamonds.sort()

for i in range(z):
    hold=-1
    for j in range(hold+1,x):
        if clients[i][0]>diamonds[j][0] and clients[i][1]<=diamonds[j][1]:
            sale+=1
            hold=j
            break
print(sale)