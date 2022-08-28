n=input()
x=n[::-1]
a=[]
b=[]
c=0
z='AEIOUaeiou'
for i in range(len(n)//2):
    if x[i] in z and n[i] not in z:
        if x[i]!=' ':
            if n[i]!=' ':
                c+=1
    elif x[i] not in z and n[i] in z:
        if x[i]!=' ':
            if x[i]!=' ':
                c+=1
    
    

print(c)

    