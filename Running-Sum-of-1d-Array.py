# Problem:
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

Solution:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        op = []
        op1 = 0
        for i in nums:
            op1 += i 
            op.append(op1)
        print(repr(op).replace(" ", ""))
        return op
