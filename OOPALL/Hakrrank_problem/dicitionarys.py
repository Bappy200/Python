if __name__ == '__main__':

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores



    def query (names):
        add = sum(student_marks.get(names))
        return add/3



    query_name = input()
    result = query(query_name)
    print('{:.2f}'.format(result))

