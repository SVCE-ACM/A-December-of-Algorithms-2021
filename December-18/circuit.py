n=int(input())
grid=[]
for i in range(n):
    grid.append(list(map(int,input().split())))
x=-1
y=-1
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            if x==-1:
                x=i
                y=j
            else:
                if x>i:
                    s=x-i
                else:
                    s=i-x 
                if y>j:
                    s+=y-j
                else:
                    s+=j-y 
print(s-1)

