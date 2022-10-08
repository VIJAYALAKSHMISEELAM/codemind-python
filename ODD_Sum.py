n=int(input())
a=list(map(int,input().split()))
od=0
for i in a:
    if(i%2!=0):
        od+=i

print(od)