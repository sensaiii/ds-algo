a=[3]
l=len(a)
v=666
if l==0 or l==1 and v!=a[l-1]:
    print("false")
for x in range(l-1):
    if a[x]==v:
        print("true",x)