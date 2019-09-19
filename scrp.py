a=0
def rec(x):
    global a
    a=x

    while x == 6:
        return x
    return x + rec(x + 1)


print(rec(1))
print(a)




def x():
    global a


