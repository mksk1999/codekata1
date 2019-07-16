a=list(map(str,input().split()))
b=len(a[0])
c=len(a[1])
s=min(b,c)
if(b>c):
    d=b-c
elif(c>b):
    d=c-b
else:
    d=0
for i in range(s):
    if((c==1 or b==1) and (a[1][i] in a[0] or a[0][i] in a[1])):
        break
    if(a[0][i]!=a[1][i]):
        d+=1 
print(d)
