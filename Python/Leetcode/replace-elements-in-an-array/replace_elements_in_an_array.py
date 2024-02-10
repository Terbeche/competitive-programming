class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dict = {num: i for i, num in enumerate(nums)}

        for operation in operations:
                num_index = nums_dict[operation[0]]
                nums[num_index] = operation[1]
                nums_dict[operation[1]] = num_index
                del nums_dict[operation[0]]

        return nums
