def insertionsort(a):
    for x in range(1, len(a)):
        curval = a[x]
        curindx = x
        while curindx > 0 and curval < a[curindx - 1]:
            a[curindx] = a[curindx - 1]
            curindx -= 1
        a[curindx] = curval
    return a


