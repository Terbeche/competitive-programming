from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        answer = []
        count = 0
        counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)

        for key, val in counter:
            if count == k:
                break
            answer.append(key)
            count += 1
        
        return answer