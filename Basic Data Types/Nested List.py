if __name__ == '__main__':
    n = int(input())
    students = []
    for i in range(n):
        students.append([input(), float(input())])
    scores = list([x[1] for x in students])
    scores.sort()
    a = scores[0]
    while(scores[1] == a):
        scores.remove(a)
    students = [x[0] for x in students if x[1] == scores[1]]
    for s in sorted(students):
        print(s)
        