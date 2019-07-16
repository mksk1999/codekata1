a=list(map(str,input().split()))
b=len(a[0])
c=len(a[1])
s=min(b,c)
if(b>c):
    d=ord(a[0][-1])-96
elif(c>b):
    d=ord(a[0][-1])-96
else:
    d=0
for i in range(s):
    if(a[0][i]!=a[1][i]):
        d+=abs(ord(a[0][i])-ord(a[1][i]))
print(d)
