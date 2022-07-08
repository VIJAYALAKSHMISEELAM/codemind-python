l=int(input())
r=int(input())
arr=[]
for i in range(l,r+1):
    arr.append(i)
c=0
for i in range(len(arr)):
    s=0
    for j in range(i,len(arr)):
        s+=arr[j]
        if(s%2!=0):
            c+=1
print(c)