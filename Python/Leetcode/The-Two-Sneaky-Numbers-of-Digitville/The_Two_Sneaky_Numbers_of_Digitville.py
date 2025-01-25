from typing import Counter, List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_dict = Counter(nums)
        answer = []

        for k, v in nums_dict.items():
            if v == 2:
                answer.append(k)
            if len(answer) == 2:
                break
        return answer
