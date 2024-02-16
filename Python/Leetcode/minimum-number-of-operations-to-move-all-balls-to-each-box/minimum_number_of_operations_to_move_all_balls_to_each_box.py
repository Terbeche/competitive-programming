class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []

        for i in range(len(boxes)):
            minimum_operations_number = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    minimum_operations_number += abs(j - i)

            result.append(minimum_operations_number)

        return result
