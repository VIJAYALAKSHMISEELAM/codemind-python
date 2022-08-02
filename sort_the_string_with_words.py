st=input()
st=st.lower()
st=st.split()
s=[]
for i in st:
    if i==" ":
        continue
    if i not in s:
        s.append(i)
print(*sorted(s))
    