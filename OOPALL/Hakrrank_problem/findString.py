def count_substring(string, sub_string):

    count = 0
    str_len=len(string)
    sub_len=len(sub_string)-1
    for i in range(str_len - sub_len):
        if sub_string == string[i:len(sub_string)+i]:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count_substring(string, sub_string)
