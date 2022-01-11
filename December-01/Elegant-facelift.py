n=int(input("Size of array"))
arr=[]
print("Enter elements of the array")
for i in range(n):
    x=input()
    arr.append(x)
occ={}
i=0
j=i+1
a=list(set(arr[i])&set(arr[j]))
for i in arr:
    check=0
    for k in a:
        for j in range(len(i)):
            if k==i[j]:
                check=1 
                break
        if check==0:
            a.remove(k)
print(len(a))
            