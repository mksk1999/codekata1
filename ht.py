n=int(input())
a=list(map(int,input().split()))
b=[]
l=len(a)
for i in range(l):
    if(a[i]==i):
        b.append(i)
b.sort()
for i in b:
    print(i,end=" ")
