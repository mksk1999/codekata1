n=int(input())
s=list(map(int,input().split()))
for i in s:
    if s.count(i)==1:
        b=s.count(i)
        c=i
print(c)
