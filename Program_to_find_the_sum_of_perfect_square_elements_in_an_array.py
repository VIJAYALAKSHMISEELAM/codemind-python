n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    d=int(i**0.5)
    if(d*d==i):
        sum+=i
print(sum)
        
    