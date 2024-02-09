if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr = sorted(list(set(arr)))
    print(new_arr[len(new_arr) - 2])
