a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i%10==0 ):
        while(i):
            d=i%10
            i=i//10
            c+=1
        if c==0:
            print(i)
    else:
        c=0
        k=0
        temp=i
        while(i):
            d=i%10
            i=i//10
            if temp%d==0:
                k+=1
            c+=1
    if(c==k):
        print(temp,end=' ')
            