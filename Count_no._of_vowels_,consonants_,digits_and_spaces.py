n=input()
v=0
c=0
d=0
s=0
z='aeiouAEIOU'
for i in n:
    if(i in z):
        v+=1
    elif(i not in z):
        if(i.isdigit()):
            d+=1
        elif(i==' '):
            s+=1
        else:
            c+=1
print('Vowels: '+str(v))
print('Consonants: '+str(c))
print('Digits: '+str(d))
print('White spaces: '+str(s))

            