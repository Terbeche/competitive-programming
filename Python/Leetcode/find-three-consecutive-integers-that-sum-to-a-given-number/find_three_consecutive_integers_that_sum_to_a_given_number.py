class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        consecutive_integers = []

        for i in range(num // 3 -1, num // 3 + 3):
            if i*3 + 3 == num:
                consecutive_integers.append(i)
                consecutive_integers.append(i + 1)
                consecutive_integers.append(i + 2)
                break
        return consecutive_integers
