n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    i=abs(i)
    i=str(i)
    r=len(i)
    if(r==k):
        c+=1
print(c)
