def bin(a,val):
    if len(a)==0 or (len(a)==1 and a[0]!=val):
        return False
    mid=a[len(a)//2]
    if val==mid:
        return True
    if val<mid:
        return bin(a[:len(a)//2],val)
    if val>mid:
        return bin(a[len(a)//2+1:],val)
a=[1,2,3,4,5,6]
print(bin(a,4 ))