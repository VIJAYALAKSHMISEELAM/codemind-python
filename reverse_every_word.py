n=input()
n=n.split()
l=[]
for i in n:
    l.append(i[::-1])
print(*l)