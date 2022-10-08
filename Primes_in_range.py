def is_it_prime(i):
    
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if(i==1):
        continue
    elif(is_it_prime(i)):
        c+=1
print(c)