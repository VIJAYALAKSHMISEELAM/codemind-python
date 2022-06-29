n=int(input())
a=list(map(int,input().split()))
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(*even,end=' ')
print(*odd,end='')

        
