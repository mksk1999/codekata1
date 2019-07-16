n=int(input())
a=list(map(int,input().split()))
def uniq(input):
    s=len(input)
    output=[]
    for x in range(s):
        k=x+1
        for j in range(k,s):
            if((input[x] == input[j]) and input[x] not in output):
                output.append(input[x])
    else:
        print("unique")
    for i in output:
        print(i,end=" ")
if(len(a)==n):
    uniq(a)
