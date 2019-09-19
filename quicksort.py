def arr(n, r):
    from random import randint
    a = [randint(1, r) for _ in range(n)]
    return a


l = arr(5, 20)

from random import randint


def quicksort(a):
    if len(a) <= 1: return a
    piv = a[randint(0, len(a) - 1)]
    print("piv",piv)
    s, e, l = [], [], []
    print("a",a)
    for x in a:
        if x > piv:
            l.append(x)
        elif x < piv:
            s.append(x)
        else:
            e.append(piv)
    print("small",s,"equal",e,"large",l)
    return quicksort(s) + e + quicksort(l)

x=[26, 9, 42, 32, 24, 50, 19, 50, 45, 18]
print(quicksort(x))