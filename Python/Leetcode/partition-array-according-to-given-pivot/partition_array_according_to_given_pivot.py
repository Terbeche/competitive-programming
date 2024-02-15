class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        less_than_pivot = []
        great_than_pivot = []
        equal_to_pivot = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                less_than_pivot.append(nums[i])
            elif nums[i] > pivot:
                great_than_pivot.append(nums[i])
            else:
                equal_to_pivot.append(nums[i])

        result = less_than_pivot + equal_to_pivot + great_than_pivot


        return result
