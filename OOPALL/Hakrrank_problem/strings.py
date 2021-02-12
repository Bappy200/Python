def swap_case(s):

    l =''

    for i in s:

        if i >= 'a' and i <= 'z':
            l +=i.upper()

        elif i >= 'A' and i <= 'Z':
            l += i.lower()

        else:
            l +=i

    return l


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)