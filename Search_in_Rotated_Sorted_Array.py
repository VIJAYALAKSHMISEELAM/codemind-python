n=int(input())
a=list(map(int,input().split()))
s=int(input())
for i in range(0,n):
    if(a[i]==s):
        print(i)
        break
else:
    print('-1')

    