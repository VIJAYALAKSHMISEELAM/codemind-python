t=int(input())
while(t):
    c=0
    a=input()
    b=input()
    for i in range(len(a)):
            if ord(a[i])<=ord(b[i]):
                c+=1
    if(c==len(a)):
        print('YES')
    else:
        print('NO')
                
    t-=1
                