n=int(input())
a=list(map(int,input().split()))
ev=0
od=0
for i in range(n):
    if(i%2==0):
        ev+=a[i]
    else:
        od+=a[i]

print(abs(ev-od))