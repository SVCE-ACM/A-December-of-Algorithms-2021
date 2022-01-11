n=int(input("Enter a number"))
sum=0
arr=[]
check=0
while sum!=1:
    while(n!=0):
        sum=sum+((n%10)**2)
        n=n//10
    if sum==1:
        check=1
        break
    elif sum not in arr:
        n=sum
        arr.append(sum)
        sum=0
    elif sum in arr:
        break
if check==1:
    print("YES")
else:
    print("NO")