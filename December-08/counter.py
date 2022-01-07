t=int(input())
if t==0:
    print(0)
    exit()
else:
    d=0
    hold=0
    j=0
    count=0
    while t>d:
        count+=1
        hold=d
        d=d+3*pow(2,j)
        j+=1
    print(3*pow(2,j-1)-(t-hold)+1)
    