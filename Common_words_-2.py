s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
l=s1.split()
k=s2.split()
c=0

for i in l:
    if i in k:
        if(l.count(i)==1 and k.count(i)==1):
            c+=1
print(c)
        
        
        
        
        