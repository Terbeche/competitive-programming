from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        answer = 0

        for i in range(0, n, 2):
            answer += nums[i]            

        return answer