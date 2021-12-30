br=list(map(int,input().split()))
n=int(input())

s=sum(br)
if s%n==0:
    ef=s//n
else:
    ef=(s//n)+1


round=1
t=0
for i in range(len(br)):
    if t+br[i]>ef:
        t=br[i]
        round+=1
    else:
        t+=br[i]
    # print(t,ef,round)
# round+=1
print(ef)
print(round,t)

if round==n:
    print(ef)
    exit()
else:
    # print("o",round,n)
    while(round>n):
        
        ef+=1
        # print(ef)
        t=0
        round=1
        for i in range(len(br)):
            if t+br[i]>ef:
                t=br[i]
                round+=1
            else:
                t+=br[i]
        round+=1
        # print(round,n)
        break

    print(ef)

