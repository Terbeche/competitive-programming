from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        for word in words:
            if word[0:len(pref)] == pref:
                answer += 1
        
        return answer