test_cases_number  = int(input())

for _ in range(test_cases_number):
    cells = list(map(int, input().split()))

    matrix_size = cells[0]
    first_cell = cells[1:3]
    second_cell = cells[3:] 

    first_comparaison = min(abs(first_cell[0] - 1), abs(first_cell[0] - matrix_size), abs(first_cell[1] - 1), abs(first_cell[1] - matrix_size))
    second_comparaison = min(abs(second_cell[0] - 1), abs(second_cell[0] - matrix_size), abs(second_cell[1] - 1), abs(second_cell[1] - matrix_size))

    print(abs(first_comparaison - second_comparaison))