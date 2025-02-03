from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        answer = 0
 
        for i in range(n):
            if  (nums[i] + diff in nums) and (nums[i] + 2 * diff in nums):
                answer += 1
        
        return answer