from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)
        answer = 0

        for i in range(n):
            for j in range(m):
                if nums1[i] % (nums2[j] * k) == 0:
                    answer += 1

        return answer