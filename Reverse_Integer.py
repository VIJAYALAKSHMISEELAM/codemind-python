n=int(input())
rev=0
temp=n
if n<0:
    n=abs(n)
while(n):
    d=n%10
    n=n//10
    rev=(rev*10)+d
if(temp<0):
    print(-rev) #print('-',rev) ani rayaku
else:
    print(rev)
