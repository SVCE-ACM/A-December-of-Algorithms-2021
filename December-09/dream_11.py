n=int(input())
p=int(input())
ns=list(map(int,input().split()))
ns.sort(reverse=True)
tot=999
hold=-1
t=0
q=p

while q<=n:
    c=0
    for k in range(t+1,q):
        c+=ns[k-1]-ns[k]
    if c<tot:
        tot=c
        hold=q
    q+=1
    t+=1
final=0
# print(ns)
for j in range(hold-p,hold):
    # print(ns[j])
    final+=ns[hold-p]-ns[j]
print(final)


    
