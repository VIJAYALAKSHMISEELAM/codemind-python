n=int(input())
l=list(map(int,input().split()))
k=[]
c=0
for i in l:
    if(l.count(i)==i):
        c+=1
        k.append(i)
k=set(k)
if(c==0):
    
    print('-1')
else:
    print(min(k),end=' ')
    print(max(k))
