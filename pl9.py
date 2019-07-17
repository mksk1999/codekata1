a=list(map(str,input().split()))
l=len(a[0])
c=0
for i in range(l):
    if(a[0][i]!=a[1][i]):
        c+=1
if(c==1):
    print("yes")
else:
    print("no")
