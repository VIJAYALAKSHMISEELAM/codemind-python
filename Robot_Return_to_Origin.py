x=input()
c=0
k=0
if x=='LL' or x=='RR' or x=='UU' or x=='DD':
    print("False")
else:
    for i in x:
        
        if i in 'UD':
            c+=1 
        elif i in 'RL':
            k+=1
    if c==2 or k==2:
        
        print("True")
    else:
        print("False")