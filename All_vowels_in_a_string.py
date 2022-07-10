n=input()
k=['a','e','i','o','u']
for i in k:
    if(i not in n):
        print('False')
        break
else:
    print('True')