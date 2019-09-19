def sel(a):
    for x in range(len(a)):
        min = x
        for y in range(x, len(a)):
            if a[min] > a[y]:
                a[y], a[min] = a[min], a[y]
    return a


a = [3, 4, 5, 1, 2]
print(sel(a))


def selection(a):
    sortlen = 0
    while sortlen < len(a):
        min = None
        for x, y in enumerate(a[sortlen:]):
            if min == None or y < a[sortlen]:
                min = x + sortlen
        a[min], a[x] = a[x], a[min]
        sortlen += 1


def inserion(a):
    for x in range(1, len(a)):
        curi = x
        curv = a[x]
        while curi > 0 and curv < a[curi - 1]:
            a[curi] = a[curi - 1]
            curi -= 1
        a[curi] = curv
    return a


x = [2, 4, 5, 2, 1, 5, 9]
print(inserion(x))


def bubble(a):
    swapped = True
    while swapped:
        swapped = False
        for x in range(len(a) - 1):
            if a[x + 1] < a[x]:
                a[x], a[x + 1] = a[x + 1], a[x]
                swapped = True
    return a
a=[3,4,5,1,2]
print("bubble",bubble(a))