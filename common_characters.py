s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
k=0
s=[]
for i in s2:
    if i in s1:
        if i==" ":
            continue
        if i not in s:
            s.append(i)

k=sorted(s)
if(len(k)==0):
    print("-1")
else:
    for i in k:
        print(i,end="")