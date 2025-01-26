from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        mix = []
        answer = ""

        for i in range(n):
            mix.append([indices[i], s[i]])

        mix.sort()

        for i in range(n):
            answer += mix[i][1]

        return answer