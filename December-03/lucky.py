n=int(input())
t=[]
for i in range(n):
    t.append(list(map(str,input().split())))
x=input()
name=[ch for ch in x]
x=-1
y=-1
for k in range(n):
    for l in range(n):
        if t[k][l]==name[0]:
            x=k
            y=l 
for j in range(1,len(name)):
    if t[x+1][y]==name[j]:
        x=x+1 
    elif t[x][y+1]==name[j]:
        y=y+1
    elif t[x+1][y+1]==name[j]:
        x=x+1
        y=y+1
    elif t[x-1][y]==name[j]:
        x=x-1 
    elif t[x][y-1]==name[j]:
        y=y-1
    elif t[x-1][y-1]==name[j]:
        x=x-1
        y=y-1
    else:
        print("NO")
        exit()
print("YES")
