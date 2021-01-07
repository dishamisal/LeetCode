# Problem:
# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

Solution:
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # nums_set = set(nums)
        # for index, value in enumerate(nums):
            # print(index, value)
            # print(nums[index])
            # nums1 = nums-nums[index]            
            # nums.pop(index)
            # print(nums)
            # print(nums1)
        # d = {}
        # # d = {value: index for value in nums}
        # for index, value in enumerate(nums):
        #     d = dict(zip(value, index))
        
        counter = 0
        for i, j in enumerate(nums):
            for k, l in enumerate(nums):
                # print(i)
                # print(j)
                if i < k and j == l:
                    counter += 1
        print(counter)
        return counter
