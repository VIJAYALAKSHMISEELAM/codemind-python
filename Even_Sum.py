n=int(input())
a=list(map(int,input().split()))
ev=0
for i in a:
    if(i%2==0):
        ev+=i

print(ev)