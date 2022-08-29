x=int(input())
ascichr=65
for i in range(x,0,-1):
    for j in range(i):
        print(chr(ascichr+x-1),end=' ')
    ascichr-=1
    print()