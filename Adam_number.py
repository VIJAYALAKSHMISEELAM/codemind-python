n=int(input())
a=n*n
rev=0
while(n!=0):
    d=n%10
    rev=(rev*10)+d
    n=n//10
b=rev*rev
c=0
while(b!=0):
    d=b%10
    c=(c*10)+d
    b=b//10
if(a==c):   #asalu num ni square chesaka vachina number should be equal to
#reverse of b-->b is rev of a square
#note:vice versa will give hidden test cases fail
    print('True')
else:
    print('False')

    
    