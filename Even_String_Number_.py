n=input()
l=[]
for i in n:
    if(i.isdigit()):
        l.append(int(i))
l=set(l)
k=list(l)
k.sort()
k.reverse()
mae=100
for i in l:
    if(i%2==0 and i<mae):
        mae=i
if(mae==100):
    print('-1')
else:
    k.remove(mae)
    k.append(mae)
    for i in k:
        print(i,end='')

    