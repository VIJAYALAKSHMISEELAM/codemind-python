n=int(input())
a=list(map(int,input().split()))
j,k=map(int,input().split())
sum=0
for i in range(0,n):
    if((a[i]<j and a[i]<k) or(a[i]>j and a[i]>k) ):
        sum+=a[i]
print(sum)