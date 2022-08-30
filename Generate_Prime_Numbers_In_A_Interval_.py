def is_it_prime(i):
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return False
    else:
        return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(is_it_prime(i)):
        if(i==1):
            continue
        else:
            print(i)
        