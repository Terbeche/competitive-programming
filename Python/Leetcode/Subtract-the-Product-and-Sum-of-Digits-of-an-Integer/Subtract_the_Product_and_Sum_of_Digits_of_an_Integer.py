class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_ = 0
        product = 1
        n_string = str(n)

        for num in (n_string):
            sum_ += int(num)
            product *= int(num)

        return product - sum_