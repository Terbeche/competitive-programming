from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        answer = 0

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    answer += 1
                else:
                    break
        
        return answer