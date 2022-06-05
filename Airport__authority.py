n=int(input())
a=[]
sum=0
for i in range(n):
    ele=int(input())
    a.append(ele)
t=int(input())
for i in range(n):
    if a[i]>t:
        sum+=2
    else:
        sum+=1
print(sum)
    