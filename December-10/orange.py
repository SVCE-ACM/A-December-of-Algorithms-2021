n=int(input())
farm=[]
for i in range(n):
    farm.append(list(map(int,input().split())))

orange=0
x=0
y=0
last=0
i=0
j=0

# print(farm)

while(i<n and j<n):
    # print(i,j)
    if i+1<n and farm[i+1][j]==1:
        x=i+1
        i=x
        farm[i][j]=0
        orange+=1
    elif j+1<n and farm[i][j+1]==1:
        y=j+1
        j=y
        farm[i][j]=0
        orange+=1
    elif i+1<n and farm[i+1][j]==0:
        x=i+1
        i=x 
    elif j+1<n and farm[i][j+1]==0:
        y=j+1
        j=y 
    
    elif i==n-1 and j==n-1:
        break
    else:
        last=-1
        break
if last==-1:
    print("last not reached")
    print(orange)
    exit()
else:
    i=0
    j=0
    while(x>0 and y>0):
        # print(x,y)
        if x-1>=0 and farm[x-1][y]==1:
            i=x-1
            x=i
            farm[x][y]=0
            orange+=1
        elif y-1>=0 and farm[x][y-1]==1:
            j=y-1
            y=j
            farm[x][y]=0
            orange+=1
        elif x-1>=0 and farm[x-1][y]==0:
            i=x-1
            x=i 
        elif y-1>=0 and farm[x][y-1]==0:
            j=y-1
            y=j
        else:
            break
    print(orange)


        
