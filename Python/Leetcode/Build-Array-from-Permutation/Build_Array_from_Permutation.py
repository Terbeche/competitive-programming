from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)

        for i in range(n):
            answer.append(nums[nums[i]])
        
        return answer