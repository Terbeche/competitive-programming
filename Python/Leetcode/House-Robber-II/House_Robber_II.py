class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            rob1, rob2 = 0, 0

            for house in nums:
                temp = max(house + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2

        return max(helper(nums[1:]), helper(nums[0:-1]))