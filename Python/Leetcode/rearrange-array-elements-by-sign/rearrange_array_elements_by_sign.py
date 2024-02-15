class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result_nums = []
        positive_numbers = []
        negative_numbers = []

        for num in nums:
            if num < 0:
                negative_numbers.append(num)
            else:
                positive_numbers.append(num)

        for i in range(len(nums)//2):
            result_nums.append(positive_numbers[i])
            result_nums.append(negative_numbers[i])
        
        return result_nums
