# Problem:
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

Solution:
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        final_list = []
        for i in nums:
            counter = 0
            for j in nums:
                # print(j)
                if i > j:
                    counter += 1
            # print(counter)
            final_list.append(counter)
        print(final_list)
        return(final_list)
