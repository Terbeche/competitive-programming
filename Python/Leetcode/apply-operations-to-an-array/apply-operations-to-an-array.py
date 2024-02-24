class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums) -1 ):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            else:
                continue
        
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(nums[i])
        
        zero_numbers = len(nums) - len(result)
        
        result.extend([0] * zero_numbers)
        
        return (result)
