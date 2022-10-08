n=int(input())
a=list(map(int,input().split()))
ev=0
od=0
for i in a:
    if(i%2==0):
        ev+=i
    else:
        od+=i

print(abs(ev-od))