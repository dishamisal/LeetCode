# Problem:
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Solution:
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # print(n)
        n = str(n)
        product = 1
        addition = 0
        for i in n:
            product = product * int(i)
            addition += int(i)
        # print(product)
        # print(addition)
        difference = product - addition
        return difference

