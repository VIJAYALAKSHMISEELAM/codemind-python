n=input()
a=list(n.split())
for i in a:
    ma='A'
    mi='z'
    for j in a[0]:
            if(ord(j)<ord(mi)):
                mi=j
    for j in a[len(a)-1]:
        if(ord(j)>ord(ma)):
            ma=j
print(mi,ma,end='')
        
            
    