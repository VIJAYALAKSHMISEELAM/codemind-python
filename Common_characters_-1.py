n=input()
n=n.lower()
l=n.split()
k=l[0]
c=0
for i in k:
    for j in l:
        if i in j:
            continue
        else:
            break
    else:
        print(i,end='')
        c+=1
if(c==0):
    
    print('-1')
    