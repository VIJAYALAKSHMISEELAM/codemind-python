n=int(input())
rev=0
temp=n
while n:
    d=n%10
    n=n//10
    rev=(rev*10)+d
n=temp
if(n==rev):
    print('True')
else:
    print('False')
    
    