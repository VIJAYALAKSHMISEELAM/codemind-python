def is_it_prime(i):
    
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return True
    return False
a=int(input())
c=0
for i in range(1,a+1):
    if(a%i==0):
        if(is_it_prime(i)):
            c+=1
print(c+1)