n=int(input())
t=int(input())
while(t):
    a,b=map(int,input().split())
    if(a<n or b<n):
        print('UPLOAD ANOTHER')
    elif(a>=n and b>=n):
        if(a==b):
            print('ACCEPTED')
        else:
            print('CROP IT')
    t-=1