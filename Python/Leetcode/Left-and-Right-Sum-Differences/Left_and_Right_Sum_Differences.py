from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        right_sum = [0]

        start_left = 0
        start_right = 0
        
        n = len(nums)

        for i in range(n-1):
            start_left += nums[i]
            left_sum.append(start_left)

        for i in range(n-1, 0, -1):
            start_right += nums[i]
            right_sum.append(start_right)
        
        right_sum.reverse()
        answer = []

        for i in range(n):
            answer.append(abs(left_sum[i] - right_sum[i]))
        return answer