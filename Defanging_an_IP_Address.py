n=input()
m=[]
for i in n:
    if(i=='.'):
        m.append('[')
        m.append('.')
        m.append(']')
    else:
        m.append(i)
for i in m:
    print(i,end='')