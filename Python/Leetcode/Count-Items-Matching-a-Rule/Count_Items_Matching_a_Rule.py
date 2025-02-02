from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer = 0

        n = len(items)

        for i in range(n): 
            if ruleKey == "type" and ruleValue == items[i][0]:
                answer += 1
                continue
            if ruleKey == "color" and ruleValue == items[i][1]:
                answer += 1
                continue
            if ruleKey == "name" and ruleValue == items[i][2]:
                answer += 1
                continue
        
        return answer