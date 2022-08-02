s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
k=0
s=[]
for i in s2:
    if i not in s1:
        if i==" ":
            continue
        if i not in s:
            s.append(i)
for i in s1:
    if i not in s2:
        if i==" ":
            continue
        if i not in s:
            s.append(i)
k=sorted(s)
for i in k:
    print(i,end="")