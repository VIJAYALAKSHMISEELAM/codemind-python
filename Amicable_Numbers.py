def is_it_ambient(m,n):
    sum=0
    for i in range(1,m):
        if m%i==0:
            sum=sum+i
    if sum==n:
        return True
    else:
        return False
m=int(input())
n=int(input())
if(is_it_ambient(m,n)):
    m,n=n,m
    if(is_it_ambient(m,n)):
        print('Amicable')
    else:
        print('Not Amicable')
else:
    print('Not Amicable')