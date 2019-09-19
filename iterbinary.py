pos = -1


def bin(a, val):
    l = 0
    u = len(a) - 1
    while l <= u:
        mid = (l + u) // 2
        if a[mid] == val:
            globals()['pos'] = mid
            return mid
        else:
            if a[mid] < val:
                l = mid
            else:
                u = mid


list = [1, 2, 4, 5, 6, 7]
v = 6
print(bin(list, v))
