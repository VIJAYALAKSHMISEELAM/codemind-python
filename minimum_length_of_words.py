n=input()
b=len(n)
c=0
for i in range(0,b):
    if(i<b):
        if(n[i]==' '):
            print(c)
            break
        else:
            c+=1
else:
    print(c)