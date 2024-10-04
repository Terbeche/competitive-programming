class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        n = len(nums)

        dp = {}
        def helper(i , total):
            if i == n:
                return total == target

            if (i, total) in dp:
                return dp[(i, total)]

            if total > target:
                return False

            dp[(i, total)] = helper(i + 1, total) or helper(i + 1, total + nums[i])
            return dp[(i, total)] 

        return helper(0, 0)
