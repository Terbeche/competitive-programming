from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer =  set()
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                answer.add(nums2[i])

        return list(answer)