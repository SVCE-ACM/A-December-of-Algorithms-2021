num=int(input())
c=[]
a=[]
for i in range(num):
    c.append(list(map(int,input().split())))
for i in range(2):
    a.append(list(map(int,input().split())))
b=[]
for i in range(len(a)):
    if a[i] in c:
        b.append("true")
    else:
        b.append("false")
print(b)
