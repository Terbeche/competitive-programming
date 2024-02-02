class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        left = 0
        right = len(x_str) - 1

        while left < right:
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1

        return True
