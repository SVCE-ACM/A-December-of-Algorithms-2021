t=list(map(int,input().split()))
pc=[]
nc=[]
for i in range(len(t)):
    if t[i]>0:
        pc.append(t[i])
    else:
        nc.append(t[i])
pc.sort()
nc.sort()
t=[]
if len(pc)>len(nc):
    for j in range(len(pc)):
        if len(nc)==0:
            for k in range(j,len(pc)):
                t.append(pc[k])
            break
        if pc[j]>(nc[0]*-1):
            t.append(pc[j])
            nc.remove(nc[0])
        elif pc[j]<(nc[0]*-1):
            # print(pc[j],nc[0])
            t.append(nc[j])
            nc.remove(nc[0])

print(t)