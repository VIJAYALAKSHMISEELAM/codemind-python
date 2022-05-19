n=int(input())
max=0
while(n!=0):
    d=n%10
    if d>max:
        d,max=max,d
    n=n//10
print(max)
    