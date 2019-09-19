from random import randint


def merg(a, b):
    c = []
    aind = 0
    bind = 0
    while aind < len(a) and bind < len(b):
        if a[aind] > b[bind]:
            c.append(b[bind])
            bind += 1
        else:
            c.append(a[aind])
            aind += 1
    if aind == len(a):
        c.extend(b[bind:])
    else:
        c.extend(a[aind:])
    return c


def merg(a, b):
    aind = 0
    bind = 0
    c = []
    while aind < len(a) and bind < len(b):
        if a[aind] < b[bind]:
            c.append(a[aind])
            aind += 1
        else:
            c.append(b[bind])
            bind += 1
    if aind < len(a):
        c.extend(a[aind:])
    else:
        c.extend(b[bind:])
    return c


def mergsort(a):
    if len(a) <= 1:
        return a
    left, right = mergsort(a[:len(a) // 2]), mergsort(a[len(a) // 2:])
    return merg(left, right)


a = [3, 4, 1, 2, 5]
print(mergsort(a))


def bubble(a):
    swapped = True
    while swapped:
        swapped = False
        for x in range(len(a) - 1):
            if a[x + 1] < a[x]:
                a[x], a[x + 1] = a[x + 1], a[x]
                swapped = True
    return a


a = [3, 4, 5, 1, 2]
print("bubble", bubble(a))


def quicksort(a):
    if len(a) <= 1:
        return a
    piv = randint(0, len(a))
    s, e, l = [], [], []
    for x in a:
        if x < a[piv]:
            s.append(x)
        elif x > a[piv]:
            l.append(x)
        else:
            e.append(x)
    return quicksort(s) + e + quicksort(l)


a = [3, 4, 5, 2, 1]
print("quick", quicksort(a))
