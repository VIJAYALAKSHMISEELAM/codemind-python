s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
l=[]
for i in s1:
    if i in s2:
        if i not in l:
            if(i==' '):
                continue
            else:
                l.append(i)
for i in s2:
    if i in s1:
        if i not in l:
            if(i==' '):
                continue
            else:
                l.append(i)
print(len(l))