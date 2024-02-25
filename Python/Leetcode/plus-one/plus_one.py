class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits and all(num == 9 for num in digits):
            digits[0] = 1
            for i in range(1, len(digits)):
                digits[i] = 0
            digits.append(0)
        
            return digits
        
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1

        else:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] != 9:
                    digits[i] += 1
                    break
                digits[i] = 0

        return digits
