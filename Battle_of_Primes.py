def is_it_prime(i):
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return 0
    else:
        return 1
d1=int(input())
d2=int(input())
a=d1+d2
for i in range(1,10):
    k=a+i
    if(is_it_prime(k)):
        print(i)
        break
    
    