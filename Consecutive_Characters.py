n=input()
c=1
z=[]
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        c+=1
    else:
        z.append(c)
        c=1
z.append(c)
print(max(z))
        