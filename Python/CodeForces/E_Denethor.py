test_cases = int(input())


for i in range(test_cases):
    array_size = int(input())
    first_array = list(map(int, input().split()))
    second_array = list(map(int, input().split()))

    i = len(first_array) - 1
    j = len(second_array) - 1
    answer = array_size

    while i >= 0 and j >= 0:
        if first_array[i] == second_array[j]:
            i -= 1
            j -= 1
            answer -= 1
        else:
            i -= 1
    
    print(answer)