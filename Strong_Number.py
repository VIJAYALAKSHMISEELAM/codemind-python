def factorial(i):
    if(i==0):
        return 1
    else:
        return i*factorial(i-1)
n=int(input())
temp=n
sum=0
while(n!=0):
    i=n%10
    k=factorial(i)
    sum+=k
    n=n//10
n=temp
if(sum==n):
    print('The number '+str(n)+' is a strong number')
else:
    print('The number '+str(n)+' is not a strong number')
    

    
