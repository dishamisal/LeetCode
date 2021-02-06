# Problem:
# We are given a list nums of integers representing a list compressed with run-length encoding.
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0). 
# For each such pair, there are freq elements with value val concatenated in a sublist.
# Concatenate all the sublists from left to right to generate the decompressed list.
# Return the decompressed list.

# Example
# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

# Solution:
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        dict = {}
        for i, j in enumerate(nums):
            if i % 2 == 0:
                val = j
            else:
                freq = j
                dict[freq] = val
                lis = []
                for k, v in dict.items():
                    lis = [k] * v
                    print(lis)
                    # for i in lis:
        lis1 = []
        lis_final = []
        for k, v in dict.items():
            # lis1.append([k] * v)
            lis1 = lis1 + ([k] * v)
            print(lis1)
        return lis1
