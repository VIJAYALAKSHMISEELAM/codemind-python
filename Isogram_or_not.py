st=input()
for i in st:
    if(st.count(i)>1):
        print(False)
        break
else:
    print(True)