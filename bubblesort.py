from random import randint


def carry(l=10, max=50):
    return [randint(1, max) for _ in range(l)]

a=carry()
print(carry())
def bsort(a):
    swapped=True
    while swapped:
        swapped=False
        for x in range(len(a)-1):
           if a[x+1]<a[x]:
               a[x],a[x+1]=a[x+1],a[x]
               print(a)
               swapped=True
    return a
a=[3,4,1,5,2]
print(bsort(a))