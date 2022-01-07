x=input()
war=[ch for ch in x]
u=[]
t=[]
for i in range(len(war)):
    if war[i]=="U":
        u.append(i)
    else:
        t.append(i)
side_u=sum(u)/len(war)
swap=0
if side_u<len(war):
    for i in range(len(u)):
        j=0
        if u[i]>=len(u):
            hold=u[i]
            u[i]=t[j]
            t[j]=hold
            j+=1
            swap+=1
print(swap)

