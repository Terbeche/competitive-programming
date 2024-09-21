from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        stack = []
        max_third_element = float('-inf')
        
        for num in reversed(nums):
            if num < max_third_element:
                return True
            while stack and stack[-1] < num:
                max_third_element = stack.pop()
            stack.append(num)
        
        return False
