number_of_words = int(input())

for i in range(number_of_words):
    word = input()

    left, right = 0, len(word) - 1
    min_letters_changes = 0

    while left <= right:
        if word[left] != word[right]:
            min_letters_changes += 1
        left += 1
        right -= 1

    print(min_letters_changes)