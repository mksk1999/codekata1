n=int(input())
s=input()
a=['a','e','i','o','u','A','E','I','O','U']
b=[]
for j in s:
    if(j not in a):
        b.append(j)
c=(b[::-1])
for i in c:
    print(i,end="")
