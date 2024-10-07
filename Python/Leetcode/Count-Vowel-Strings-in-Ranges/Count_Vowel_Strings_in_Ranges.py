from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        n = len(words)

        prefix_sum = [0] * (n + 1) 

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i + 1] += 1
        
        answer = []
        for start, end in queries:
            answer.append(prefix_sum[end + 1] - prefix_sum[start])

        return answer
