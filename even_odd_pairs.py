n=int(input())
l=list(map(int,input().split()))
ev=[]
od=[]
k=[]
for i in range(len(l)):
    if(l[i]%2==0):
        ev.append(l[i])
    else:
        od.append(l[i])
if(len(ev)>len(od)):
    for i in range(len(od)):
        k.append(ev[i])
        k.append(od[i])
    for i in range(len(od),len(ev)):
        k.append(ev[i])
    if(n%2==0):
        print(*k)
    else:
        k.append(0)
        print(*k)
elif(len(ev)<len(od)):
    
    for i in range(len(ev)):
        
        k.append(ev[i])
        k.append(od[i])
    for i in range(len(ev),len(od)):
        k.append(od[i])
    if(n%2==0):
        print(*k)
    else:
        k.append(0)
        print(*k)
else:
    for i in range(len(od)):
        k.append(ev[i])
        k.append(od[i])
    print(*k)
        