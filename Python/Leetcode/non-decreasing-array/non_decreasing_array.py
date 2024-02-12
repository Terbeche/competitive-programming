class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        necessary_modifications_number = 0

        for i in range(len(nums)- 1):
            if nums[i] > nums[i + 1]:
                necessary_modifications_number += 1
                if necessary_modifications_number > 1:
                    return False
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]

        return True
