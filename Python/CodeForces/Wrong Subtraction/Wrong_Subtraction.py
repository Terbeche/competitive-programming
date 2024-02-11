my_number, number_of_substractions = map(int, input().split())
 
for _ in range(number_of_substractions):
    if my_number % 10 == 0:
        my_number = my_number // 10
    else:
        my_number -= 1
 
print(my_number)
