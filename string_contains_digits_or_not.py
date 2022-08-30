t=int(input())
while t:
    n=input()
    for i in n:
        if(i.isdigit()):
            print('Yes')
            break
    else:
        print('No')