n=input()
k=n.lower()
r=k.split()
c=0
for i in r:
    if(i==i[::-1]):
        c+=1
print(c)
        