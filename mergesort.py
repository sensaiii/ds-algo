# merges two sorted arrays a & b
def merge(a, b):
    print("a",a)
    print("b",b)
    c = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    print("c",c)
    return c


# performs merge sort on the input array
def merge_sort(a):
    print("A",a)
    # a list of zero or one elements is sorted, by definition
    if len(a) <= 1: return a
    # split the list in half and call merge sort recursively on each half
    left, right = merge_sort(a[:len(a) // 2]), merge_sort(a[len(a) // 2:])
    print("left",left)
    print("rigt",right)
    # merge the now-sorted sublists
    return merge(left, right)


def create_array(size=6, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]


a = [3,4,1,2,5]
print(a)
a = merge_sort(a)
print
a
