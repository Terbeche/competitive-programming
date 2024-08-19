tt = int(input())

for _ in range(tt):
    num = input()
    num = num[::-1]
    solutions = ["00", "52", "05", "57"]
    answer = float("inf")

    def solve(num, solution):
        i = 0
        j = 0

        while i < len(num) and j < 2:
            if num[i] == solution[j]:
                i += 1
                j += 1
            else:
                i += 1

        if j == 2:
            return i - 2
        else:
            return float("inf")


    for solution in solutions:
        answer = min(answer, solve(num, solution))
    print(answer)