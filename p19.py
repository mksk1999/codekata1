def prime(b):
    for i in range(2,b):
        if b%i==0:
            break
    else:
        if b!=1:
            print(b,end=" ")
        
a=int(input())
for i in range(1,a+1):
    if a%i==0:
        prime(i)
