class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largest_perimeter = 0
        nums_sorted = sorted(nums, reverse = True)
        
        for i in range(len(nums_sorted) - 2):
                if nums_sorted[i] <  (nums_sorted[i+1] + nums_sorted[i+2]):
                    return nums_sorted[i] + nums_sorted[i+1] + nums_sorted[i+2]
                else:
                    continue

        return largest_perimeter