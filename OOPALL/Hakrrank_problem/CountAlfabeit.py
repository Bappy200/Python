

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        sl=string[i:i+k]
        a=[]
        for j in sl:
            if j not in a:
                a.append(j)
        for t in a:
            print(t,end='')
        print()


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)