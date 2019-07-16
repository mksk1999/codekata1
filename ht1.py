n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
l=len(a)
for i in range(l):
    if(a[i]==i):
        b.append(i)
    else:
        c+=1
if(c==l):
    print("-1")
b.sort()
for i in b:
    print(i,end=" ")

