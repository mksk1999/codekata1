n=int(input())
a=list(map(int,input().split()))
a.sort()
b=a[::-1]
l=len(a)
c=0
for i in range(l):
    if(b[i]==0):
        c+=1
if(c==l):
    print("0")
else:
    for i in b:
        print(i,end="")
