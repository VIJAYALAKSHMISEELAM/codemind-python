n=int(input())
a=list(map(int,input().split()))
j,k=map(int,input().split())
c=0
for i in range(0,n):
        if((a[i]<j and a[i]<k) or(a[i]>j and a[i]>k) ):
            c+=1
            print(a[i],end=' ')
if(c==0):
    print("-1")