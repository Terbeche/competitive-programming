class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            for letter in word:
                letter_ = chr((ord(letter) + 1 - ord('a')) % 26 + ord('a'))
                word += letter_

        return word[k-1]