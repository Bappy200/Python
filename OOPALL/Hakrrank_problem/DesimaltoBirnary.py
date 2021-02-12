def print_formatted(number):
    # your code goes here
    p = len(str(bin(number)))-1
    l = p-1

    for i in range(1,number+1):
        print('{0:{2:d}d}{0:{1:d}o}{3:>{1:d}}{0:{1:d}b}'.format(i,p,l,str(hex(i))[2:].upper()))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)