n=input()
c=0
k=n.split()
z='AEIOUaeiou'
for i in range(len(k)):
    a=k[i]
    b=a[::-1]
    for i in range(len(a)//2):
        if a[i] in z and b[i] not in z:
            if a[i]!=' ':
                if b[i]!=' ':
                    
                    c+=1
        elif a[i] not in z and b[i] in z:
            if a[i]!=' ':
                if b[i]!=' ':
                    c+=1
    
    
    

print(c)

    