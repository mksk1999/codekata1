l,r=map(int,input().split())
b=[]
for i in range(1,100000):
    if(i%l==0 and i%r==0):
        b.append(i)
b.sort()
print(b[0])
