s=input()
b=0
for i in s:
    if s.count(i)>b:
        b=s.count(i)
        c=i
print(c)
