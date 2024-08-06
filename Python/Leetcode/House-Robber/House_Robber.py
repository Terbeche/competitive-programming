from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for house in nums:
            temp = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
