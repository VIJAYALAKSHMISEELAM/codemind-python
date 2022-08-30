n=int(input())
a=0
b=1
print(a,b,end=' ')
c=2
while(True):
    k=a+b
    c+=1
    a=b
    b=k
    print(k,end=' ')
    if(c==n):
        break
    