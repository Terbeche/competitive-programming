test_cases = int(input())

reference = "codeforces"
for i in range(test_cases):
    the_string  = input()
    counter = 0
    for i in range(10):
        if the_string[i] != reference[i]:
            counter += 1
    print(counter)