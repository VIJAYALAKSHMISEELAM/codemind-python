n=int(input())
a=list(map(int,input().split()))
od=0
for i in range(n):
    if(i%2==0):
        od+=a[i]

print(od)