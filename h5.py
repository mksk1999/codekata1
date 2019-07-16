n=int(input())
a=list(map(int,input().split()))
l=len(a)
for i in range(l):
    if(i%2==0 and a[i]%2!=0):
        print(a[i],end=" ")
    elif(i%2!=0 and a[i]%2==0):
        print(a[i],end=" ")

