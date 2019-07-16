n=int(input())
a=list(map(int,input().split()))
count=dict()
for word in a:
    if word not in count:
        count[word]=1
    else:
        count[word]+=1
for word in a:
    if (count[word]==1):
        print(word)


