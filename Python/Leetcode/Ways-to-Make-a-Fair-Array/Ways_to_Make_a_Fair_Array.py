from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        right_odd = sum(nums[1::2])
        right_even = sum(nums[::2])
        left_odd = 0 
        left_even = 0
        answer = 0
        n = len(nums)

        for i in range(n):
            if i % 2 == 0:
                right_even -= nums[i]
            else:
                right_odd -= nums[i]
            
            if left_odd + right_even == left_even + right_odd:
                answer += 1
            
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]
        
        return answer