our_string = input()

the_max = 0
rings_counter = 0

for i in range(len(our_string)):
    if our_string[i] == "O":
        rings_counter += 1
        the_max = max(the_max, rings_counter)

    else:
        rings_counter = 0

print(the_max)