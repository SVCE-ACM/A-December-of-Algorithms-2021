n=int(input())
while n>9:
    t=0
    while n>0:
        t=t+((n%10)*(n%10))
        n=n//10
    if t==1:
        print("YES")
        exit()
    n=t
print("NO")

