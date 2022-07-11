s=input()
a=list(s.split())
for i in a:
    ma='z' 
    mi='A'
    for j in i:
        if ord(j)<ord(ma):
            ma=j 
        if ord(j)>ord(mi):
            mi=j
    print(ord(mi)-ord(ma),end=' ')