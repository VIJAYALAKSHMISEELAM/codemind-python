n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
        sum+=i
b=sum/n
print("{:.2f}".format(b))