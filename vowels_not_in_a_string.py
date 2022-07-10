n=input()
c=0
k=['a','e','i','o','u']
for i in k:
    if(i not in n):
        print(i,end=' ')
        c+=1
if(c==0):
    print('0')
    