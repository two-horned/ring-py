base     = int(input("Enter base: "))
tosearch = int(input("Enter number from which you search the inverse for: "))

def seek(a,b):
    c = (b // a + 1)
    d = (c * a) % b
    e = c
    while d != 1:
        c = (b // d + 1)
        d = (c * d) % b
        e *= c
    return e % b

e = seek(tosearch,base)
print(e)
