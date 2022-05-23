a,b=map(int,input().split())
d=int(a%pow(10,b))
rev=0
while a!=0:
    r=a%10
    a=a//10
    rev=(rev*10)+r
f=int(rev%pow(10,b))
e=0
while(f!=0):
    r=f%10
    f=f//10
    e=(e*10)+r
print(abs(d-e))
    