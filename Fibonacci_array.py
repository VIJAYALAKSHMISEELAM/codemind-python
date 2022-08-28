n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(3,n):
    if(a[i-1]+a[i-2]==a[i]):
        c+=1
        
if(c+3==n):
    print("yes")
else:
    print("no")