if __name__ == '__main__':
    s = input()
    c = False

    def check(r):
        global c
        c = False
        if r:
            print(True)
        else:
            print(False)

    for i in s:
        if i.isalnum():
            c = True
            break
    check(c)

    for i in s:
        if i.isalpha():
            c = True
            break
    check(c)

    for i in s:
        if i.isdigit():
            c = True
            break
    check(c)

    for i in s:
        if i.islower():
            c = True
            break
    check(c)
    for i in s:
        if i.isupper():
            c = True
            break
    check(c)


