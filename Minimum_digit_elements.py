n=int(input())
a=list(map(int,input().split()))
v=[]
c=0
for i in a:
    i=abs(i)
    i=str(i)
    k=len(i)
    v.append(k)
mine=min(v)
for i in a:
    i=abs(i)
    i=str(i)
    k=len(i)
    
    if(k==mine):
        c+=1
print(c)


    
    