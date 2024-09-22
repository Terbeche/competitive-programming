if __name__ == '__main__':
    N = int(input())
    
    answer = []
    
    for _ in range(N):
        command = input().split()
        
        if command[0] == 'insert':
            i, e = map(int, command[1:])
            answer.insert(i, e)
        elif command[0] == 'print':
            print(answer)
        elif command[0] == 'remove':
            e = int(command[1])
            answer.remove(e)
        elif command[0] == 'append':
            e = int(command[1])
            answer.append(e)
        elif command[0] == 'sort':
            answer.sort()
        elif command[0] == 'pop':
            answer.pop()
        elif command[0] == 'reverse':
            answer.reverse()
            
