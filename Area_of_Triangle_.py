a,b,c=map(int,input().split())
s=(a+b+c)/2
res=s*(s-a)*(s-b)*(s-c)
area=res**0.5
print("%.2f"%area)