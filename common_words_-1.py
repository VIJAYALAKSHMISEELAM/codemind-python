s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=s1.split()
b=s2.split()
l=[]
for i in a:
    if i in b:
        if i==' ':
            continue
        else:
            l.append(i)
print(len(l))