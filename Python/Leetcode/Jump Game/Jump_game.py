class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        max_point = 0
        for i in range(len(nums) - 1):
            max_point = max(max_point, i + nums[i])
            if max_point >= len(nums) - 1:
                return True
            if max_point <= i:
                return False
        return False
