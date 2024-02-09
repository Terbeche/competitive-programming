if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        operation = input().split()
        
        if operation[0] == "print":
            print(list)
        elif operation[0] == "pop":
            list.pop()
        elif operation[0] == "sort":
            list.sort()
        elif operation[0] == "reverse":
            list.reverse()
        elif "insert" == operation[0]:
            list.insert(int(operation[1]), int(operation[2]))
        elif "append" == operation[0]:
            list.append(int(operation[1]))
        elif "remove" == operation[0]:
            list.remove(int(operation[1]))
