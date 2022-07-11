n=input()
a=list(n.split())

for i in a:
    ma='A'
    mi='z'
    for j in i:
        if(ord(j)<ord(mi)):
            mi=j
        if(ord(j)>ord(ma)):
            ma=j
    print(mi,ma,end=' ')
    
    