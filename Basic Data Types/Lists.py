List = []
n = int(input())

for i in range(n):
    operation, *parse = input().split()
    parse = list(map(int, parse))
    if(operation == "remove"):
        List.remove(parse[0])
    elif(operation == "pop"):
        List.pop()
    elif(operation == "sort"):
        List.sort()
    elif(operation == "insert"):
        List.insert(parse[0], parse[1])
    elif(operation == "append"):
        List.append(parse[0])
    elif(operation == "print"):
        print(List)
    elif(operation == "reverse"):
        List.reverse()