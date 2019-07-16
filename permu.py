import itertools
s=int(input())
a=str(s)
l=list(itertools.permutations(a))
for i in range(len(l)):
    print(*l[i],sep='')

