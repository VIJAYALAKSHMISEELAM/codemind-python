t=int(input())
while t:
    n=input()
    k=n[::-1]
    if(n==k):
        if(len(n)%2==0):
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')
    t-=1