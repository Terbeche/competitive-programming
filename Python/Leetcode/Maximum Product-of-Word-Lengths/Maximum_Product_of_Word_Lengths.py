from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        answer = 0
        binary = [0] * len(words)
        
        for i in range(len(words)):
            for char in words[i]:
                binary[i] |= 1 << (ord(char) - ord('a'))

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not(binary[i] & binary[j]):
                    answer = max(answer, len(words[i]) * len(words[j]))

        return answer