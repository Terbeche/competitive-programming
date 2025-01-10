from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = nums
        answer.extend(answer)

        return answer