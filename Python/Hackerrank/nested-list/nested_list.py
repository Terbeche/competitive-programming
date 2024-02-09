if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    second_low = sorted(list(set([score for name, score in records])))[1]
    students = sorted([name for name, score in records if score == second_low])

    for student in students:
        print(student)