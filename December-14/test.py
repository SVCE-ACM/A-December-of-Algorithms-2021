n=list(map(int,input().split()))
x=int(input())
sum=0
for i in range(len(n)):
    sum+=n[i]
if sum%x==0:
    hr=sum//x 
else:
    hr=(sum//x)+1 
# print("hr=",hr)
hour=0
for j in range(len(n)):
    if n[j]%hr==0:
        hour+=n[j]/hr
    else:
        hour+=(n[j]//hr)+1

if hour==x:
    print(hr)
    exit()
else:
    while(hour>x):
        hr+=1
        hour=0
        for j in range(len(n)):
            if n[j]%hr==0:
                hour+=n[j]/hr
            else:
                hour+=(n[j]//hr)+1
    
print(hr)

