def chack_str(string):
    result=''
    for i in string:
        count = string.count(i)
        if count > 1:
            if i not in result:
                result +=i
        else:
            result+=i
    return result

def merge_the_tools(string,k):
    length = len(string)//k
    for i in range(length,len(string)+length,length):
        r = i-length
        re=chack_str(string[r:i])
        print(re)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
