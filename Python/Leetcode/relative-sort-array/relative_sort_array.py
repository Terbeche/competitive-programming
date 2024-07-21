class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        answer = []
        
        for num in arr2:
            answer.extend([num] * count[num])
            del count[num]
        
        for num in sorted(count.keys()):
            answer.extend([num] * count[num])
        
        return answer
