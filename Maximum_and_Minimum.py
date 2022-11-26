n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if(i==a.count(i)):
        b.append(i)
if(len(b)==0):
    print('-1')
else:
    print(min(b),end=" ")
    print(max(b),end=" ")
    
    