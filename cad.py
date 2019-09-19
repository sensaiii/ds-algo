x=0
def call(l, b):
    global x

    while True:
        if l == 1 or b == 1:
            x += l * b
            return
        if l > b :

            dif = l - b
            if l - dif == b:
                x+=1
                call(dif, b)
        elif l < b :
            dif = b - l
            if l == b - dif:
                x += 1
                call(l, dif)
        return x


print(call(5, 3))
print(x)

