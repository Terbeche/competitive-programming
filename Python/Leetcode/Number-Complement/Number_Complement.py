class Solution:
    def findComplement(self, num: int) -> int:
        count = 0
        num_copy = num

        while(num_copy != 0):
            num_copy = num_copy>>1
            count += 1
        
        return  num ^ (2 ** count -1)