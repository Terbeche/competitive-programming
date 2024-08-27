from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def solve(i, current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0
                   
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            add = solve(i + 1, current_sum + nums[i])
            subtract = solve(i + 1, current_sum - nums[i])

            memo[(i, current_sum)] = add + subtract
            return memo[(i, current_sum)]

        return solve(0, 0)