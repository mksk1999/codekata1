import itertools
s=input()
l=list(itertools.permutations(s))
for i in range(len(l)):
    print(*l[i],sep='')
