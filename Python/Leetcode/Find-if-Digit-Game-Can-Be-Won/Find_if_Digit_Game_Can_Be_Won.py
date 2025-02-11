from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit = 0
        double_digit = 0

        for num in nums:
            if num < 10:
                single_digit += num
            else:
                double_digit += num
        
        return double_digit != single_digit