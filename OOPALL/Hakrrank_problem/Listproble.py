if __name__ == '__main__':
    N = int(input())
    l=[]
    while N > 0:
        query = input().split()

        if query[0] == 'insert':
            l.insert(int(query[1]), int(query[2]))
        elif query[0] == 'print':
            print(l)
        elif query[0] == 'remove':
            l.remove(int(query[1]))
        elif query[0] == 'append':
            l.append(int(query[1]))
        elif query[0] == 'sort':
            l.sort()
        elif query[0] == 'pop':
            l.pop()
        elif query[0] == 'reverse':
            l.reverse()
        N -= 1