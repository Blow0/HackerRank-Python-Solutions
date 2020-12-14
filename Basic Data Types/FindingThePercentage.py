if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        #The unpacking operator * assigns the first input to name and the rest to line.
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    List = student_marks[query_name]
    Avg = sum(List) / len(List)
    print("%.2f" % Avg)