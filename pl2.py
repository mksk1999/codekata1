s=int(input())
def fact(s):
    if(s==1):
        return 1
    else:
        return s*fact(s-1)
if(s>0):
    print(fact(s))
elif(s==0):
    print(1)


