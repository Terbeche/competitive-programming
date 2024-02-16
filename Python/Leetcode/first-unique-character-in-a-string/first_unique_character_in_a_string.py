from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counts = Counter(s)

        for i in range(len(s)):
            if s_counts[s[i]] == 1:
                return i

        return -1
