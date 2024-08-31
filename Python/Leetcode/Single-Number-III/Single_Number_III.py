from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        diff_bit = 1
        while not (xor & diff_bit):
            diff_bit = diff_bit << 1
        
        x, y = 0, 0
        for num in nums:
            if diff_bit & num:
                x = x ^ num
            else:
                y = y ^ num
        
        return [x, y]