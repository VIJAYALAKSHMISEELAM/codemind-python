x=input()
x=x.lower()
s=x.split()
l=[]
k=s[0]
c=0
for i in k:
    for j in s:
        if(i==' '):
            continue
        elif i in j:
            continue
        else:
            break
    else:
        c+=1
        l.append(i)
if(c==0):
    print("-1")
else:
    print(min(l))
        
        
