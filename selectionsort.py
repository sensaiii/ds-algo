def selection(a):
    sortlen = 0
    print("sortlen",sortlen)
    while sortlen < len(a):
        min = None
        for x, val in enumerate(a[sortlen:]):
            print(x)
            if min == None or val < a[sortlen]:
                min = x + sortlen
        a[sortlen], a[min] = a[min], a[sortlen]
        sortlen += 1
        print(a)
        print("sortlen",sortlen)
    return a


a = [32, 4, 6, 23, 2, 564]
print(selection(a))


def sel(a):
    for x in range(len(a) - 1):
        min = x
    for y in range(x, len(a)):
        if a[y] < a[min]:
            min = y
    a[x], a[min] = a[min], a[x]
    return a
print(sel(a))