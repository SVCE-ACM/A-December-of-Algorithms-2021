t=list(map(str,input().split()))
n=len(t)
neck=dict()
for i in range(n):
    t[i]=''.join(set( t[i]))
    for j in range(len(t[i])):
        if t[i][j] in neck :
            neck[t[i][j]]+=1 
        else:
            neck[t[i][j]]=1
hold=0
for x in neck.values():
    if x==n:
        hold+=1
print(hold)
