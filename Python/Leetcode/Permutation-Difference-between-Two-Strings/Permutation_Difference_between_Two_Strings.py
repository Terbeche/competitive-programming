from collections import defaultdict


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        n = len(s)
        answer = 0
        occurence = defaultdict(list)

        for i in range(n):
            occurence[s[i]].append(i)
            occurence[t[i]].append(i)

        for v in occurence.values():
            answer += abs(v[0] - v[1])

        return answer